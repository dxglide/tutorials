# https://www.pythontutorial.net/python-basics/python-args/
# https://www.pythontutorial.net/python-basics/python-kwargs/

# Python uses the same concept for the function arguments. 
# It’s like tuple unpacking except that the args is a tuple, not a list. For example:
# x, y, *z = 10, 20, 30, 40

# print(x)
# print(y)
# print(z)


def add(x, y, *args):
    total = x + y
    for arg in args:
        total += arg

    return total


result = add(10, 20, 30, 40)
print(result)


# In Python, the parameters like *args are called variadic parameters.
#  Functions that have variadic parameters are called variadic functions.
# Note that you don’t need to name args for a variadic parameter. 
# For example, you can use any meaningful names like *numbers, *strings, *lists, etc.
# However, by convention, Python uses the *args for a variadic parameter.

# The *args parameter must be the last parameter in the function definition.

def add(*args):
    print(args[0])
    print(args[1])
    print(args[2])
add(1, 2, 3)

# You need to use a keyword argument after the *args argument as follows:
def add(x, y, *args, z):
    return x + y + sum(args) + z
add(10, 20, 30, 40, z=50)


print("----  Unpacking a tuple with an asterisk  ---- ")
def point(x, y):
    return f'({x},{y})'
a = (0, 0)
origin = point(*a)
print(origin)

print("----  KWARGS  ---- ")

# In Python, a function can have a parameter 
# preceded by two stars (**). For example: **kwwargs
# The **kwargs is called a keyword parameter.
# When a function has the **kwargs parameter,
#  it can accept a variable number of keyword arguments as a dictionary.
# The two stars (**) are important. However, the name kwargs
#  is by convention. Therefore, you can use any other meaningful names such as **configs and **files.

def connect(**kwargs):
    print(kwargs)


config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

connect(**config)


print("----  Using both *args and **kwargs arguments  ---- ")
def fn(*args, **kwargs):
    print(args)
    print(kwargs)
fn(1, 2, x=10, y=20)