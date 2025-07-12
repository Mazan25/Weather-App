import requests
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    print("Speaking:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("weather.mp3")
    playsound("weather.mp3")
    os.remove("weather.mp3")  # Delete after playing

def get_weather(city):
    api_key = "17dbcb2d568e2a5389e89cc10a6dda3d"  # Replace with your real OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            speak("Sorry, I couldn't find the city.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        report = f"The weather in {city} is {desc}, with a temperature of {temp} degrees Celsius and humidity of {humidity} percent."
        speak(report)
    except Exception as e:
        speak("Something went wrong.")
        print("Error:", str(e))

# Run the program
speak("Welcome to the weather app.")
city = input("Enter city name: ")
if city:
    get_weather(city)
else:
    speak("You didn't enter a city name.")
