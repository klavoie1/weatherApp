import tkinter as tk
from tkinter import messagebox
import weatherApi

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    lat, lon = weatherApi.get_city_coordinates(city)
    if lat is None or lon is None:
        messagebox.showerror("Error", "City not found. Please try again.")
        return
    
    weather_data = weatherApi.get_weather_data(lat, lon)
    if weather_data:
        display_weather(weather_data)

def display_weather(data):
    current_weather = data["current"]
    daily_forecast = data["daily"]
    
    result_label.config(text=f"Current: {current_weather['weather'][0]['description'].capitalize()}, "
                             f"{current_weather['temp']}°C\n"
                             f"Humidity: {current_weather['humidity']}%\n"
                             f"Wind Speed: {current_weather['wind_speed']} m/s")
    
    forecast = "\n".join([f"Day {i+1}: {day['temp']['day']}°C, {day['weather'][0]['description']}" 
                          for i, day in enumerate(daily_forecast[:7])])
    forecast_label.config(text=f"7-Day Forecast:\n{forecast}")

# Tkinter GUI
root = tk.Tk()
root.title("Weather Forecast App")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=fetch_weather).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

forecast_label = tk.Label(root, text="", justify="left")
forecast_label.pack(pady=10)

root.mainloop()
