def greet(name):
    print(f"Hi {name}")

greet('yes im :) ')

def greetReturn(name):
    return f"Hi {name}"

print (greetReturn('yes, return '))


def greetReturn(name, msg='defualt_name'):
    return f"Hi {name} and your message  {msg}"
print (greetReturn('valio', 'pranesimas'))
print (greetReturn('no_name'))

def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

net_price = get_net_price(100)
print(net_price)

net_price = get_net_price(price=100, discount=0.06)
print(net_price)

net_price = get_net_price(100, discount=0.06)
print(net_price)

#The following will result in an error because it uses the positional argument after a keyword argument:
# net_price = get_net_price(100, tax=0.08, 0.06)
# SyntaxError: positional argument follows keyword argument


print ("----- RECURSIVE FUNCTIONs  ------- ")
def count_down(start):
    """ Count down from a number  """
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)


count_down(3)


def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0
result = sum(100)
print(result)


print ("-----  LAMBDA  ------- ")

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name} {first_name}"
)
print(full_name)

# Functions that return a function example
def times(n):
    return lambda x: x * n

triple = times(3)
print(triple(2))  # 6
print(triple(3))  # 9


# he problem is that all the there lambda expressions reference the i variable,
#  not the current value of i. When you call the lambda expressions, the value of the variable i is 3.
# To fix this, you need to bind the i variable to each lambda expression at the time 
# the lambda expression is created. One way to do it is to use the default argument:

callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())


def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

add.__doc__

help(add)