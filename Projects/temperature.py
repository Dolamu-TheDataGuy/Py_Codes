#Temperature convert from Fahrenheit to celsius

Fahrenheit_temp = int(input("Please enter temperature in Fahrenheit: "))

Celsius_temp = ((Fahrenheit_temp - 32) * (5/9))

Celsius_temp = round(Celsius_temp,2)

print(Celsius_temp)

print(f"{Fahrenheit_temp} Fahrenheit is the same as {Celsius_temp} Celsius")


