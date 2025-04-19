# Weather-Report-App
🌦️ Weather App GUI — A Python desktop application that fetches and displays real-time weather data using OpenWeatherMap API. Built with Tkinter for the UI &amp; Pillow for image handling. Includes weather icons, city-based search, and a clean interface.


## 🚀 Features

- Search for current weather conditions by city name
- Displays:
  - City name
  - Weather condition (e.g., Clear, Rain)
  - Temperature
  - Weather icon
- Reset and Exit functionality
- Responsive weather icon display
- Stylish background UI with `Tkinter`

## 🛠️ Tech Stack

- Python 3
- Tkinter (GUI)
- Pillow (Image handling)
- Requests (HTTP requests)
- OpenWeatherMap API


## 📦 Installation

1. **Clone the repository**
   
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   
3. **Install dependencies**
   ```bash
   pip install pillow requests

4. **Run the App**
   ```bash
   python main.py

## 🌐 Setup API Key

This app uses OpenWeatherMap for weather data.
  - Create an account and get your API key.
  - Replace the API key in main.py:
    
    ```bash
    weather_key = 'YOUR_API_KEY'

## 📁 Project Structure

    weather-app/
    ├── img/                     # Folder for weather icons
    │   ├── 01d.png
    │   └── ...
    ├── blue.jpg                # Background image
    ├── get_weather_icons.py    # Script to download OpenWeatherMap icons
    ├── main.py                 # Main GUI app
    └── README.md               # Project info

## 💡 How It Works
- User enters a city name
- App fetches weather info via OpenWeatherMap API
- The formatted result and relevant icon are displayed


## ✨ Screenshot
![image alt](https://github.com/rajatbansod/Weather-Report-App/blob/main/Screenshot%202025-04-18%20122719.png)

![image alt](https://github.com/rajatbansod/Weather-Report-App/blob/main/Screenshot%202025-04-18%20122700.png)


## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.


## 📄 License
 ```bash
---

Let me know if you want to include a `.gif` of the app running or tailor it further for publishing on GitHub Pages or as a Windows executable.
