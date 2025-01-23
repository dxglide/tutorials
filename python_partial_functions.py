# https://www.pythontutorial.net/python-basics/python-partial-functions/

# In Python, a partial function is a function that is created by fixing a number of arguments of a function.
#standart funtions  example
def multiply(a, b):
    return a*b
def double(a):
    return multiply(a, 2)
result = double(10)
print(result)  # 20

# Since you’ll create partial functions sometimes, Python provides you with the partial 
# function from the functools standard module to help you define partial functions more easily

print("----  Partial Functions  ---- ")
# Python partial function from functools module

from functools import partial
def multiply(a, b):
    return a*b

double = partial(multiply, b=2)

result = double(10)
print(result)

print("----  Partial Functions  variables  ---- ")
x = 2
f = partial(multiply, x)
result = f(10)  # 20
print(result)
x = 3
result = f(10)  # 20
print(result)