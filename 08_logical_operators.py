temp = 25
is_sunny = True
is_raining = False

if is_raining and is_sunny:
    print("You are going to sweat outside.")
elif temp >= 20 and not is_sunny:
    print("Maybe take an umbrella with you.")
elif temp <= 10 or temp >= 40:
    print("The event is getting cancelled.")
else:
    print("The event will be fine.")