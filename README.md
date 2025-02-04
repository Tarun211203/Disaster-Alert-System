# RiskRadar   
**Real-time Disaster Alert System with Weather Monitoring**

## Features  
- Real-time email alerts for disasters  
- User registration & location-based alerts  
- Admin dashboard for emergency broadcasts  
- Weather monitoring (OpenWeather API)  
- Responsive UI with Bootstrap 5


## Project Structure
RiskRadar/
├── app.py                 # Main application file
├── requirements.txt       # Dependencies
├── /templates             # HTML templates
├── /static                # CSS and static files
└── database.db            # SQLite database (created after first run)


## 🛠️ Setup  

### Prerequisites  
- Python 3.8+  
- Gmail account  
- [OpenWeather API Key](https://openweathermap.org/api)  

1. **Clone & Enter**   
   git clone https://github.com/Tarun211203/Disaster-Alert-System

2. **Create Virtual Environment**  
      for Windows:
      python -m venv venv && venv\Scripts\activate
      for Mac/Linux:
      python3 -m venv venv && source venv/bin/activate

3. **Install Dependencies**
      pip install -r requirements.txt

4. **Configuration**
      Gmail Setup:
        Enable 2-Step Verification
        Create App Password: App → Mail, Device → Other
      In app.py:
        replace
        app.config['MAIL_USERNAME'] = 'your.email@gmail.com'  
        app.config['MAIL_PASSWORD'] = 'your-app-password'
      OpenWeather API:
        Replace in app.py:
        OpenWeather_API = "your-api-key"

5. **Initialize Database**
       flask shell
        >>> db.create_all()
        >>> exit()

6. **Run Application**
      flask run
      Visit → http://localhost:5000



   
👥 User Guide

Regular User:
Register/Login → Dashboard → Set Location → Receive Alerts
Check weather for any city

Admin (admin@disaster.com / admin123):
Send location-based emergency alerts
Automatic email notifications to affected users

