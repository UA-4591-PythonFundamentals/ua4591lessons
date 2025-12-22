import tkinter as tk
from pyowm import OWM

API_KEY = "ef2206ff5da67de63306d0b143e20872"

# Подключаемся к сервису погоды
owm = OWM(API_KEY)
weather_manager = owm.weather_manager()


def get_weather():
    city = entry.get().strip()

    if not city:
        result_label.config(text="Please enter a city name.")
        return

    try:
        observation = weather_manager.weather_at_place(city)
        weather = observation.weather

        temp_c = weather.temperature("celsius")["temp"]
        report = (
            f"Weather: {weather.detailed_status}\n"
            f"Temperature: {temp_c}°C\n"
            f"Humidity: {weather.humidity}%"
        )
    except Exception:
        report = "City not found or error fetching weather."

    result_label.config(text=report)


# --- Интерфейс ---
root = tk.Tk()
root.title("Weather Application")
root.geometry("450x350")

top_frame = tk.Frame(root, bd=5)
top_frame.pack(padx=10, pady=10, fill="x")

entry = tk.Entry(top_frame, font=("Courier", 12))
entry.pack(side="left", expand=True, fill="x", padx=(0, 10))

button = tk.Button(top_frame, text="Get Weather", command=get_weather)
button.pack(side="left")

result_label = tk.Label(root, font=("Courier", 14), justify="left", anchor="nw")
result_label.pack(padx=10, pady=10, expand=True, fill="both")

root.mainloop()
