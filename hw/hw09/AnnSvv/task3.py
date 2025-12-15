import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        detailed_status = w.detailed_status         # 'clouds'
        wind = w.wind()                  # {'speed': 4.6, 'deg': 330}   
        humidity = w.humidity                # 87
        temperature = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        rain  = w.rain                    # {}
        heat_index = w.heat_index              # None
        clouds = w.clouds                  # 75

        result = f'''Weather in {city}: \n{detailed_status} \nWind:{wind} \nHumidity: {humidity} \nTemperature: {temperature} \nRain: {rain} \nHeat index: {heat_index} \nClouds: {clouds}'''
        label['text'] = result
    except Exception as err:
        error_message = f"Incorect data: {err}."
        label['text'] = error_message


HEIGHT = 350
WIDTH = 450


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


label = tk.Label(lower_frame, font=('Courier', 8), wraplength=300)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()