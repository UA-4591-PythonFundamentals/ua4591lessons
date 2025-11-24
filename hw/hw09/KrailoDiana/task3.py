import tkinter as tk
from pyowm import OWM

HEIGHT = 350
WIDTH = 450

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

observation = mgr.weather_at_place('London,GB')
w = observation.weather

print(w.detailed_status)         
print(w.wind())                  
print(w.humidity)                
print(w.temperature('celsius'))  
print(w.rain)                    
print(w.heat_index)              
print(w.clouds)                  

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_weather():
    
    city = entry_field.get()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    wind = w.wind()
    speed = wind.get("speed")
    deg = wind.get("deg")
    
    text = (
        f"Weather in {city}:\n"
        f"Status: {w.detailed_status}\n"
        f"Temperature: {w.temperature('celsius')['temp']} degrees Celsius\n"
        f"Wind speed {speed} m/s in the direction of {deg} degrees\n"
        f"Humidity: {w.humidity}%\n"
        f"Clouds: {w.clouds}%"
    )
    
    label.config(text=text, wraplength=300, justify="left", font = ("Times New Roman", 16))

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()