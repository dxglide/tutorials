# https://www.pythontutorial.net/python-basics/python-unpacking-tuple/

# Python defines a tuple using commas (,), not parentheses (). For example, the following defines a tuple with two elements:
# 1,2 

# ython uses the parentheses to make the tuple clearer:
# (1, 2)

# Python also uses the parentheses to create an empty tuple:
# ()

# Code language: Python (python)
# In addition, you can use the tuple() constructor like this:
# tuple()

# o define a tuple with only one element, you still need to use a comma. The following example illustrates how to define a tuple with one element:
# 1,
# Code language: Python (python)
# It’s equivalent to the following:
# (1, )


# Unpacking a tuple means splitting the tuple’s elements into individual variables.
# x, y = (1, 2)

tuplas = (1,2)
tuplai =   [tuplas, (3,4), (5,6)] 
print(type(tuplas)) 
print(type(tuplai)) 
print(tuplai)


print("----  Unpacking a tuple  ---- ")

x, y  = tuplas;
print(f"is tuplo: x={x},y={y}")


x, y ,z = 10, 20, 30
print(type(x))

numbers = 10, 20, 30
print(type(numbers))

print("----  Unpacking tuple to swap values of two variables  ---- ")
x = 10
y = 20
print(f'x={x}, y={y}')
x, y = y, x
print(f'x={x}, y={y}')

print ("----  Unpacking a tuple with an asterisk  ---- ")
r, g, *other = (192, 210, 100, 0.5)

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
numbers = (*odd_numbers, *even_numbers)
print(numbers)