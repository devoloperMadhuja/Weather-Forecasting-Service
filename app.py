from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)
API_KEY = 'a0692c7e95e85eeb0480293da7a07c8d'  # Replace with your actual OpenWeatherMap API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != '200':
        return render_template('index.html', error="City not found")

    current = data['list'][0]
    forecast = data['list'][::8]

    condition = current['weather'][0]['main']
    backgrounds = {
        "Clear": "clear.jpg",
        "Clouds": "clouds.jpg",
        "Rain": "rain.jpg",
        "Thunderstorm": "storm.jpg",
        "Snow": "snow.jpg",
        "Mist": "mist.jpg",
        "Haze": "haze.jpg"
    }
    background_image = backgrounds.get(condition, "default.jpg")

    weather_data = {
        'city': data['city']['name'],
        'country': data['city']['country'],
        'current': {
            'temp': current['main']['temp'],
            'feels_like': current['main']['feels_like'],
            'humidity': current['main']['humidity'],
            'wind': current['wind']['speed'],
            'description': current['weather'][0]['description'],
            'icon': current['weather'][0]['icon']
        },
        'forecast': [{
            'date': item['dt_txt'].split()[0],
            'description': item['weather'][0]['description'],
            'temp_min': item['main']['temp_min'],
            'temp_max': item['main']['temp_max'],
            'icon': item['weather'][0]['icon']
        } for item in forecast]
    }

    return render_template('report.html', weather=weather_data, background=background_image)

if __name__ == '__main__':
    app.run(debug=True)