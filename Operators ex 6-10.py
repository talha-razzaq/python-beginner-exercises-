#🟢 2. Operators — Exercises 6–10


#🔴6. Basic Calculator - Take two numbers and display:
# Addition # Subtraction # Multiplication# Division
print("Basic Calculate")
num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))

print("Addition")
addition = num1 + num2
print(f"The Total is: {addition}")

print("Minus")
minus = num1 - num2
print(f"The Total is: {minus}")

print("Multiply")
multiply = num1 * num2
print(f"The Total is: {multiply}")

print("Division")
division = num1 / num2
print(f"The Total is: {division}")

#🔴7. Even or Odd Using %-Take a number and determine its remainder when divided by 2.
number = float(input("Enter the number: "))
if number % 2 == 0:
    print("It is even number") 
else:
    print("It is odd number")

#🔴 8. Last Digit - Take an integer and find its last digit.# Example: # Input: 457, # Output: 7
print("Last Digit")
number = float(input("Enter the number: "))
print(number % 10)

#🔴 9. Square and Cube-# Take a number and calculate its square and cube.
number = int(input("Enter the number"))
print(number ** 2)
print(number ** 3)

#🔴 10. Percentage-# Take obtained marks and total marks and calculate percentage.

english = int(input("Enter the number; "))
math = int(input("Enter the number; "))
science = int(input("Enter the number; "))

obtain_marks = english + math + science
print("Total marks is : ", obtain_marks)

percentage = (obtain_marks / 300) * 100

print("The percentage of marks is ", percentage)
