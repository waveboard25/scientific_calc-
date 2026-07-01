def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition =", a + b)

def sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction =", a - b)

def mul():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication =", a * b)

def div():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division =", a / b)


import math


def power(base, exponent):
    return base ** exponent

def square_root(number):
    if number < 0:
        return "Error: Negative root"
    return math.sqrt(number)

def sine(angle_degrees):
    return math.sin(math.radians(angle_degrees))

def natural_log(number):
    if number <= 0:
        return "Error: Log undefined"
    return math.log(number)



