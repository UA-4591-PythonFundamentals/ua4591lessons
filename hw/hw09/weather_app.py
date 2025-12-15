from pyowm import OWM
import tkinter as tk
import os
from dotenv import load_dotenv

HEIGHT = 350
WIDTH = 450

load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left', wraplength=300)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def get_weather(location):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(location)
    w = observation.weather

    results = (f'Detailed status: {w.detailed_status}\n'
               f'Wind speed: {w.wind()["speed"]}\n'
               f'Wind direction: {w.wind()["deg"]}\n'
               f'Humidity: {w.humidity}\n'
               f'Temperature: {w.temperature("celsius")["temp"]}\n'
               f'Rain: {w.rain}\n'
               f'Heat index: {w.heat_index}\n'
               f'Clouds: {w.clouds}')

    label['text']= results

root.mainloop()
