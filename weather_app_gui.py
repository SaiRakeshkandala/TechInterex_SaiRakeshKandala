from tkinter import *
from datetime import datetime
from weather_app.api import get_weather

def fetch_weather(api_key, city_entry, result):
    """
    Fetches weather data and updates the GUI with results.
    
    Args:
        api_key (str): Your OpenWeatherMap API key.
        city_entry (Entry): The input field for the city name.
        result (StringVar): The variable to display the weather details.
    """
    city = city_entry.get()
    data = get_weather(city, api_key)
    if data.get("cod") == 200:
        result.set(
            f"City: {data['name']}\n"
            f"Temperature: {data['main']['temp']}°C\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Weather: {data['weather'][0]['description']}\n"
            f"Wind Speed: {data['wind']['speed']} m/s\n"
            f"Sunrise: {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')}\n"
            f"Sunset: {datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')}"
        )
    elif "error" in data:
        result.set(f"Error: {data['error']}")
    else:
        result.set("City not found. Please check the name.")

def gui_mode(api_key):
    """
    Launches the Tkinter-based GUI for the Weather App.
    
    Args:
        api_key (str): Your OpenWeatherMap API key.
    """
    app = Tk()
    app.title("Weather App")
    app.geometry("400x300")

    Label(app, text="Enter City:").pack(pady=5)
    city_entry = Entry(app)
    city_entry.pack(pady=5)

    result = StringVar()
    Button(app, text="Get Weather", command=lambda: fetch_weather(api_key, city_entry, result)).pack(pady=10)
    Label(app, textvariable=result, wraplength=350, justify="left").pack(pady=10)

    app.mainloop()
