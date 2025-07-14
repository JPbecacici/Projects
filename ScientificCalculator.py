# Scientific Calculator Calculator in Python

import math
print("Welcome to Python Scientific Calculator!")
print("Available operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exponentiation (^)")
print("6. Square Root (sqrt)")
print("7. Logarithm (log)")
print("8. Sine (sin)")
print("9. Cosine (cos)")
print("10. Tangent (tan)")
print("11. Factorial (factorial)")
print("12. Greatest Common Divisor (gcd)")
print("13. Least Common Multiple (LCM)")
print("14. Exit")
operator = int(input("Enter the operation number: "))

if operator == 1:
    print("1. Addition (+)")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"Result: {result}")
    print("Thank you for using Python Scientific Calculator!")
    exit() 

elif operator == 2:
    print("2. Subtraction (-)")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"Result: {result}")
    print("Thank you for using Python Scientific Calculator!")
    exit()

elif operator == 3:
    print("3. Multiplication (*)")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"Result: {result}")
    print("Thank you for using Python Scientific Calculator!")
    exit()

elif operator == 4:
    print("4. Division (/)")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        result = num1 / num2
    exit()