principal = 0
deposit = -0.01
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can´t be less than or equal to zero.")

while deposit <= -0.01:
    deposit = float(input("Enter your deposit amount: "))
    if deposit <= -0.01:
        print("Deposit can´t be less than zero.")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can´t be less than or equal to zero.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can´t be less than or equal to zero.")

principal = principal - deposit
total = principal * pow((1 + rate / 100), time)
interest = total - principal
print(f"Balance after {time} year/s: {total:.2f}€.")
print(f"You total interst paid after {time} year/s will be {interest:.2f}€. ")