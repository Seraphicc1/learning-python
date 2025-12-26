hunger = input("Are you rly hungry? (y/n): ")

if hunger == "y":
    print("Go get some food.")
elif hunger == "n":
    print("Alright good for you.")
else:
    print("Invalid answer!")

###################################

online = True

if online:
    print("User is online.")
else:
    print("User is offline.")