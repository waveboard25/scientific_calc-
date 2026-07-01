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
def cosine(angle_degrees):
    return math.cos(math.radians(angle_degrees))

def tangent(angle_degrees):
    return math.tan(math.radians(angle_degrees))

def absolute(number):
    return abs(number)

def reciprocal(number):
    if number == 0:
        return "Error: Division by zero"
    return 1 / number

def maximum(a, b):
    return max(a, b)

def minimum(a, b):


    return min(a, b)

def average(a, b):
    return (a + b) / 2

def floor_value(number):
    return math.floor(number)

def ceil_value(number)
i    return math.ceil(number)

def radians(angle):
    return math.radians(angle)

def degrees(angle):
    return math.degrees(angle)

print("Extra Functions Loaded"):





def cube_root(number):
    return number ** (1/3)

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0
