weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

# Dictionary comprehension to convert the temperature to fahrenheit
weather_f = {new_temp: ((new_value * 9/5) + 32) for (new_temp, new_value) in weather_c.items()}
print(weather_f)
