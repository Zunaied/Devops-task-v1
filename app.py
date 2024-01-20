from flask import Flask, jsonify
import platform
import datetime
import requests

app = Flask(__name__)


WEATHER_API_KEY = '8be6c8be24e1343291686eca79950e3b'
WEATHER_API_URL = f'http://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid={WEATHER_API_KEY}'

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(
        hostname=platform.node(),
        datetime=datetime.datetime.now().strftime('%y%m%d%H%M'),
        version="1.0",
        weather=fetch_weather_data()
    )

@app.route('/api/weather', methods=['GET'])
def get_weather():
    return jsonify(weather=fetch_weather_data())

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify(status='healthy')

def fetch_weather_data():
    try:
        weather_response = requests.get(WEATHER_API_URL)
        weather_data = weather_response.json()

        temperature = weather_data['main']['temp']
        temp_unit = 'C'  

        return {
            "dhaka": {
                "temperature": temperature,
                "temp_unit": temp_unit
            }
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return {"error": "Unable to fetch weather data"}

if __name__ == '__main__':
    app.run( host='0.0.0.0',debug=True, port=5500)
