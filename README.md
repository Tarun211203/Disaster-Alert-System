# RiskRadar

## Real-time Disaster Alert System with Weather Monitoring

### 📌 Features
- **Real-time Email Alerts**: Get notified instantly about disasters in your area.
- **User Registration & Location-Based Alerts**: Users can register and receive alerts based on their location.
- **Admin Dashboard**: Allows administrators to send emergency broadcasts.
- **Weather Monitoring**: Uses the [OpenWeather API](https://openweathermap.org/api) to provide real-time weather updates.
- **Responsive UI**: Built with Bootstrap 5 for a seamless user experience.

---

## 📂 Project Structure
```
RiskRadar/
├── app.py                 # Main application file
├── requirements.txt       # Dependencies
├── /templates             # HTML templates
├── /static                # CSS and static files
└── database.db            # SQLite database (created after first run)
```

---

## 🛠️ Setup

### Prerequisites
- Python **3.8+**
- A **Gmail** account (for sending email alerts)
- **[OpenWeather API Key](https://openweathermap.org/api)**

### Installation & Configuration

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Tarun211203/Disaster_Alert_CS303
cd Disaster-Alert-System
```

#### 2️⃣ Create a Virtual Environment
- **Windows**:
  ```bash
  python -m venv venv && venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  python3 -m venv venv && source venv/bin/activate
  ```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Email and API Keys
- **Gmail Setup**:
  1. Enable **2-Step Verification** in your Google account.
  2. Generate an **App Password**:
     - App → Mail
     - Device → Other
  
- **Update `app.py`**:
  Replace the placeholders with your credentials:
  ```python
  app.config['MAIL_USERNAME'] = 'your.email@gmail.com'  # Your Gmail address
  app.config['MAIL_PASSWORD'] = 'your-app-password'    # Your generated App Password
  OpenWeather_API = 'your-api-key'                      # Your OpenWeather API Key
  ```

#### 5️⃣ Initialize the Database
```bash
flask shell
>>> db.create_all()
>>> exit()
```

#### 6️⃣ Run the Application
```bash
flask run
```
Visit the app in your browser: [http://localhost:5000](http://localhost:5000)

---

## 👥 User Guide

### Regular Users
1. **Register/Login** → Create an account and log in.
2. **Set Location** → Choose your location for disaster alerts.
3. **Receive Alerts** → Get notified about emergencies.
4. **Check Weather** → View weather updates for any city.

### Admin Access
- **Login as Admin**:
  - Email: `admin@disaster.com`
  - Password: `admin123`
- **Features**:
  - Send **location-based emergency alerts**.
  - Automatically notify affected users via email.

---


## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

### 📩 Contact
For any queries, reach out at: `tarun2112203@gmail.com`

