#Our Code uses Python's Flask library to build a web-app that helps users to stay informed of any disaster possibilities near them.

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy as sqal
from flask_mail import Mail, Message
import os
from sqlalchemy import func
import requests as rq

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'                 #database.db is our database!

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP - SIMPLE MAIL TRANSFER PROTOCOL
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'Enter_User_Name'
app.config['MAIL_PASSWORD'] = 'Enter_App_Password'
app.config['MAIL_DEFAULT_SENDER']='Enter_Admin_Email'     #The Email id Used by Admin

db = sqal(app)
mail = Mail(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)             #PRIMARY KEY == OUR UNIQUE IDENTIFIER!
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)            #Passwords can't be NULL.
    location = db.Column(db.String(100), nullable=False)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():                                   # index.html -> Homepage
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        print("City entered:", city)
        weather = check_weather(city)
    
    return render_template('index.html', weather=weather)
        

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':                                            #Registration Details
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        location = request.form['location']
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for('register'))
        new_user = User(name=name, email=email, password=password, location=location)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))                              #Re-direct to Login after Registering
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']                                  #Login Details
        password = request.form['password']
        
        # Admin Login Check
        if email == 'admin@disaster.com' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))                           #Re-direct to Admin dashboard
        
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:                                                 #User not found
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)

@app.route('/edit_location', methods=['GET', 'POST'])
def edit_location():
    if 'user_id' not in session:
        return redirect(url_for('login'))                           #Re-direct to Login
    user = User.query.get(session['user_id'])
    if request.method == 'POST':
        user.location = request.form['location']                     #Add location
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_location.html', user=user)

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('admin_logged_in'):                            #Check if it is really the admin logged in
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        location = request.form['location']
        message = request.form['message']
        

        users = User.query.filter(func.lower(User.location) == location.lower()).all()   #To overcome case-sensitivity

        
        # Send emails
        with mail.connect() as conn:
            for user in users:
                msg = Message(
                    subject="Disaster Alert!",                                                #Mail Format
                    sender=app.config['MAIL_DEFAULT_SENDER'],
                    recipients=[user.email],
                    body=f"Alert for {location}: {message}"
                )
                conn.send(msg)
        
        new_alert = Alert(location=location, message=message)
        db.session.add(new_alert)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))        #Redirect to homepage
    
OpenWeather_API = "c1634204f1a0419f3f9b92634096d0b2"              #For Our Weather Widget

def check_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={OpenWeather_API}"     #OpenWeather
    response = rq.get(url)
    data = response.json()
    print("Weather API Response:", data)   #To Debug on Terminal
    if response.status_code == 200:
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
        }
        return weather
    else:
        return None


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
