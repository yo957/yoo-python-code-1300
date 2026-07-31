"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = weight / (height ** 2)

if bmi > 0 and bmi <= 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi <= 24.9:
    print("Normal weight")
elif bmi > 25.0 and bmi <= 29.9:
    print("Overweight")
elif bmi <= 30.0:
    print("Obese")


"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
rate = 35.5

print("Currency Convertor:")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Enter(1 or 2): ")

if choice == "1":
    thb = float(input("Enter amount in THB: "))
    usd = thb / rate
    print(f"Formula: {thb:.2f} / {rate} = {usd:.2f}")

elif choice == "2":
    usd = float(input("Enter amount in USD: "))
    thb = usd * rate
    print(f"Formula: {usd:.2f} * {rate} = {thb:.2f}")

