#🟢 1. Variables & Input — Exercises 1–5

#🔴1. Personal Information Ask the user for their name, age, and city and display all three.
print("Ask the user for Personal info:-")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print(f'Personal info: {name}, is from {city} city, He is {age} years old.')

#🔴2. Two Numbers Take two numbers from the user and display them.
print("Take two numbers and disply it.")
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
print(f'You have entered {num1} and {num2}.')

#🔴3. Rectangle-Take length and width and calculate the area.
print("Calculate Rectanglar area")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
rectangle = length * width
print(f'The area of rectangle is {rectangle}.')

#🔴4. Temperature- Take Celsius as input and convert it to Fahrenheit.
print("Celsius to Fahrenheit")
celsius = float(input("Enter the celsius temperture: "))
cal_fahrenhiet = (celsius * 9/5) + 32
print(f"Temperture is {cal_fahrenhiet} Fahrenhiet.")

print("Fahrenheit to Celsius")
fahrenheit = float(input("Enter the fahrenheit temperture: "))
cal_celsius = (fahrenheit - 32) * 5/9
print(f"Temperture is {cal_celsius} Celsius.")

#🔴5. Shopping #Ask for product price and quantity and calculate the total price.
print("Ask product prcie and quantity and cal total")

beg = int(input("Enter the beg price: "))
beg_qty = int(input("Enter the beg qty: "))
glasses = int(input("Enter the glasses price: "))
glasses_qty = int(input("Enter the glasses qty: "))

beg_total = beg * beg_qty
glasses_total = glasses * glasses_qty

grand_total = beg_total + glasses_total
print(f'The total of all purchase is: {grand_total}')