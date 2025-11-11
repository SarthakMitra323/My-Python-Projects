print("Welcome to the Calculator!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b    

a = input("Enter first number: ")
b = input("Enter second number: ")

while a.isalpha() or b.isalpha():
    print("Please enter valid numbers.")
    a = input("Enter first number: ")
    b = input("Enter second number: ")

a = float(a)
b = float(b)
operation = input("Enter operation (+, -, *, /, ^, %): ")

if operation == "+":
    print(f"{a} + {b} = {add(a, b)}")
elif operation == "-":
    print(f"{a} - {b} = {subtract(a, b)}")
elif operation == "*":
    print(f"{a} * {b} = {multiply(a, b)}")
elif operation == "/":
    print(f"{a} / {b} = {divide(a, b)}")
elif operation == "^":
    print(f"{a} ^ {b} = {power(a, b)}")
elif operation == "%":
    print(f"{a} % {b} = {modulus(a, b)}")
else:
    print("Invalid operation.")
