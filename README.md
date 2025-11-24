# 🌦️ Weather Forecasting Service  
**Flask + XML + SOAP (Spyne) + XSLT + OpenWeatherMap API**

A full-stack weather forecasting application that integrates REST (JSON) and SOAP (XML) services, with XSLT-based HTML transformation and a dynamic, responsive frontend.

## 📌 Project Overview
This application fetches real-time weather data, processes it through a SOAP web service, transforms XML using XSLT, and displays a modern UI with dynamic weather backgrounds.

## ✨ Features
- Real-time weather data with 5-day forecast  
- Dynamic weather-based backgrounds  
- SOAP web service (Spyne) returning XML  
- XSLT XML→HTML transformation  
- Responsive UI (HTML/CSS/JS)  
- Error handling for invalid city names  

## 🏗️ Architecture
```
User → Flask App → OpenWeatherMap API → SOAP (XML)
        ↓
     XSLT → HTML Report → Browser
```
## 🎥 Demo Video

[Click here to watch the demo](https://github.com/devoloperMadhuja/Weather-Forecasting-Service/blob/main/WhatsApp%20Video%202025-11-24%20at%2011.55.13_c0a1619e.mp4)


## 🧰 Tech Stack
Python, Flask, Spyne, XML, XSLT, HTML, CSS, JavaScript, OpenWeatherMap API

## 📂 Folder Structure
```
Weather-Forecasting-Service/
│── app.py
│── weather_service.py
│── transform.xslt
│── requirements.txt
│
├── templates/
│   ├── index.html
│   └── report.html
│
├── static/
│   ├── style.css
│   ├── clear.jpg
│   ├── clouds.jpg
│   ├── rain.jpg
│   ├── storm.jpg
│   ├── snow.jpg
│   ├── mist.jpg
│   ├── haze.jpg
│   └── default.jpg
```

## 🛠️ How to Run
```bash
git clone <your-repo-url>
cd Weather-Forecasting-Service
pip install -r requirements.txt
python app.py
```

## 🚀 Future Scope
- Geolocation  
- Weather alerts  
- 10‑day forecast  
- Weather maps  
- PWA support  

## 📜 License
MIT License
