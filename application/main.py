from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="templates")

BASE_URL = os.getenv("XWEATHER_BASE_URL")
CLIENT_ID = os.getenv("XWEATHER_CLIENT_ID")
CLIENT_SECRET = os.getenv("XWEATHER_CLIENT_SECRET")


def get_nyc_weather():
    response = requests.get(
        f"{BASE_URL}client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"
    )

    return response.json()



@app.route("/")
def index():
    weather_data = get_nyc_weather()

    location = weather_data["response"][0]["place"]["name"]
    temperature = weather_data["response"][0]["periods"][0]["tempC"]
    wind = weather_data["response"][0]["periods"][0]["windSpeedKPH"]
    humidity = weather_data["response"][0]["periods"][0]["humidity"]
    timestamp = weather_data["response"][0]["periods"][0]["timestamp"]

    display_data = {
        "location": location,
        "temperature": temperature,
        "wind": wind,
        "humidity": humidity,
        "timestamp": timestamp
    }

    return render_template("index.html", weather=display_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)