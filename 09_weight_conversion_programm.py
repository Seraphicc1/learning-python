weight = float(input("Please enter the weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "pounds"
    print(f"The weight is: {round(weight, 1)} {unit}.")
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "kilograms"
    print(f"The weight is: {round(weight, 1)} {unit}.")
else:
    print(f"{unit} was not valid.")