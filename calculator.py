##
import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be 0")
    return b / a

def log(a ,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("a and b must by greater than 0, and a cannot equal 1")
    return math.log(b) / math.log(a)

def exp(a, b):
    return a**b

def hypotenuse(a, b):
    math.hypot(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("a cannot be less than 0")
    return math.sqrt(a)
