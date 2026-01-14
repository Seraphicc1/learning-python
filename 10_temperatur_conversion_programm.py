unit = input("Is the temperature in celsius, fahrenheit or kelvin? (C, F, K): ")
temp = float(input("Enter the temperature: "))
unit2 = input("Which temperature would you like to know? (C, F, K): ")

if unit.upper() == "C" and unit2.upper() == "F":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature is {temp}F.")
elif unit.upper() == "C" and unit2.upper() == "K":
    temp = round(temp + 273.15, 1)
    print(f"The temperature is {temp}K.")
elif unit.upper() == "F" and unit2.upper() == "C":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature is {temp}C.")
elif unit.upper() == "F" and unit2.upper() == "K":
    temp = round(((temp - 32) * 5 / 9) + 273.15, 1)
    print(f"The temperatur is {temp}K.")
elif unit.upper() == "K" and unit2.upper() == "C":
    temp = round(temp - 273.15, 1)
    print(f"The temperature is {temp}C.")
elif unit.upper() == "K" and unit2.upper() == "F":
    temp = round((temp - 273.15) * 9 / 5 + 32, 1)
    print(f"The temperature is {temp}F.")
else:
    print("Invalid unit.")