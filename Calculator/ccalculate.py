import math
from functools import reduce
# Two or three input operations
def add(*args):
    return reduce(lambda a,b:a+b , args)
def subtract(*args):
    if len(args) == 2:
        return args[0] - args[1]
    elif len(args) == 3:
        return args[0] - args[1] - args[2]
    else:
        return "Subtraction requires two or three inputs."
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
def divide(*args):     
    if len(args) == 2:
        return args[0] / args[1]
    elif len(args) == 3:
        return args[0] / args[1] / args[2]
    else:
        return "Division requires two or three inputs."
def power(*args):
    return args[0] ** args[1]
# Single input operations
def square(*args):
    return args[0] ** 2
def square_root(*args):
    return args[0] ** 0.5
def percentage(*args):
    return args[0] / 100
def logarithm(*args):
    return math.log(args[0])
def sin(*angle):
    return math.sin(math.radians(angle[0]))
def cos(*angle):
    return math.cos(math.radians(angle[0]))
def tan(*angle):
    return math.tan(math.radians(angle[0]))
def factorial(*args):
    return math.factorial(args[0])
def exponential(*args):
    return math.exp(args[0])

running=1

print("A. Two or Three Inputs -\n1. Addition(+) \n2. Subtraction(-)\n3. Multiplication(*)\n4. Division(/)\n5. x to the power y(^)")
print("\nB. One Input -\n1. Square (:)\n2. Square Root(;)\n3. Percentage(%)\n4. Logarithm(`)\n5. Sin of angle(sin)\n6. Cos of angle(cos)\n7. Tan of angle(tan)\n8. Factorial(!)\n9. Exponential value of a number($)")
print('\n  (&) EXIT')

while running:
    str=input("Enter your equation").split(' ')
    equation=[int(x) for x in str]

    sign=input("Enter the sign of opration :")

    if sign=='+':
        result=add(*equation)
        print(f'Result: {result}')
    elif sign=='-':
        result=subtract(*equation)
        print(f'Result: {result}')
    elif sign=='*':
        result=multiply(*equation)
        print(f'Result: {result}')
    elif sign=='/':
        result=divide(*equation)
        print(f'Result: {result}')
    elif sign=='^':
        result=power(*equation)
        print(f'Result: {result}')
    elif sign==':':
        result=square(*equation)
        print(f'Result: {result}')
    elif sign==';':
        result=square_root(*equation)
        print(f'Result: {result}')
    elif sign=='%':
        result=percentage(*equation)
        print(f'Result: {result}')
    elif sign=='`':
        result=logarithm(*equation)
        print(f'Result: {result}')
    elif sign=='sin':
        result=sin(*equation)
        print(f'Result: {result}')
    elif sign=='cos':
        result=cos(*equation)
        print(f'Result: {result}')
    elif sign=='tan':
        result=tan(*equation)
        print(f'Result: {result}')
    elif sign=='!':
        result=factorial(*equation)
        print(f'Result: {result}')
    elif sign=='$':
        result=exponential(*equation)
        print(f'Result: {result}')
    elif sign=="&":
        running =0