from functools import reduce

numbers = [1, 3, 2, 7, 9, 4]
print(numbers[1])

print ("-----------------")
numbers = [1, 3, 2, 7, 9, 4]
print(numbers[-1])
print(numbers[-2])

print ("-----Modifying, adding, and removing elements ")
print ("-----Modifying" )
numbers = [1, 3, 2, 7, 9, 4]
numbers[0] = 10

print(numbers)

numbers = [1, 3, 2, 7, 9, 4]
numbers[1] = numbers[1]*10

print(numbers)
numbers = [1, 3, 2, 7, 9, 4]
numbers[2] /= 2

print(numbers)


print ("-----  adding ")
numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)

print(numbers)

print ("-----  adding/inserting ")
numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)

print(numbers)

print ("-----removing elements ")
numbers = [1, 3, 2, 7, 9, 4]
del numbers[0]
print(numbers)


print ("-----rremoving by pop() ")
# The pop() method removes the last element from a list and returns that element:
numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()
print(last)
print(numbers)


print ("To remove an element by value, you use the remove() method)")
numbers = [1, 3, 2, 7, 9, 4, 9]
numbers.remove(9)
print(numbers)


print ("----- TUPLES ----  ")
# A tuple is a list that cannot change. 
# Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.

rgb = ('red', 'green', 'blue')
print(rgb)


def gautiTupla(action, msg):
    if action == 'pirmas':
        return ("ACTION_VIENAS",msg)
    elif action == 'antras':
         return ("ACTION_DU",msg)
    else:
         return ("BETKOKS_ACTION",) # kai vienas

tuplas = gautiTupla('aaa', 'badom gauti tupla ....')
print(tuplas)

print ("----- SORT list ----  ")
# If a list contains strings, the sort() method sorts the string elements alphabetically.
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()
print(guests)

#reverse
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort
print(guests)

scores = [5, 7, 4, 6, 9, 8]
scores.sort()
print(scores)

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
print(companies)

# def sort_key(company):
#     return company[2]

#companies.sort(key=sort_key, reverse=True)
companies.sort(key=lambda company: company[2], reverse=True)
print(companies)

print ("----- SORTED  list ----  ")
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)

print(guests)
print(sorted_guests)

print ("----- SLICE list ----  ")
# Lists support the slice notation that allows you to get a sublist from a list:
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[1:4]
print(sub_colors)

sub_colors = colors[:3]  #To get the n-first elements from a list
print(sub_colors)
sub_colors = colors[-3:]  #To get the n-last elements of a list
print(sub_colors)
sub_colors = colors[::2]  #To get every n-th element from a list
reversed_colors = colors[::-1]  #To reverse a list
print(reversed_colors)

print ("----- SLICE list - SUBSTITUTE----  ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2] = ['black', 'white']
print(colors)

print ("----- SLICE list - SUBSTITUTE 2 ----  ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f"The list has {len(colors)} elements")

colors[0:2] = ['black', 'white', 'gray']
print(colors)
print(f"The list now has {len(colors)} elements")

print ("----- SLICE list - SUBSTITUTE  DELETE  ----  ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
del colors[2:5]
print(colors)

print ("----- LIST unapacking  ----  ")
colors = ['red', 'blue', 'green']
red, blue, green = colors
print(f"{red} {blue} {green}")  
#red, blue = colors  # ValueError: too many values to unpack (expected 2)
red, blue, *other = colors
print(f"{red} {blue} {other}") 


print ("----- LIST iteration   ----  ")
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for city in cities:
    print(city)

for item in enumerate(cities):
    print(item)
for index, city in enumerate(cities):  # used enumaration  tuple and after that unpack it
     print(f"{index}: {city}")
     
for index, city in enumerate(cities,1): #s starts from index 1 
    print(f"{index}: {city}")


print ("----- LIST  find index of element   ----  ")
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
result = cities.index('Mumbai')
print(result)

#result = cities.index('Osaka')
#print(result)  # ValueError: 'Osaka' is not in list

city = 'Osaka'
if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")

print ("----- LIST  ITERABLES or iterators   ----  ")
for index in range(3):
    print(index)
str = 'Iterables'
for ch in str:
    print(ch)
ranks = ['high', 'medium', 'low']
for rank in ranks:
    print(rank)

print ("----- Iterator   ----  ")
# An iterable can be iterated over. And an iterator is the agent that performs the iteration.
# To get an iterator from an iterable, you use the iter() function.
colors = ['red', 'green', 'blue']
colors_iter = iter(colors)
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
# print(next(colors_iter)) # StopIteration:

print ("----- Iterator in iteration   ----  ")
colors = ['red', 'green', 'blue']
iterator = iter(colors)

for color in iterator:
    print(color)

print ("-----  List() to MAP()  ----  ")
def double(bonus):
    return bonus * 2

# or iterator = map(lambda bonus: bonus*2, bonuses)

bonuses = [100, 200, 300]
iterator = map(double, bonuses)
print(list(iterator))

names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))

carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
TAX = 0.1
print(carts)

def map_price(cart):
    return [cart[0], cart[1], cart[1] * TAX]

#carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)
carts = map(map_price, carts)
print(list(carts))

print ("-----  List() and  Filter  ----  ")
scores = [70, 60, 80, 90, 50]
filtered = []
for score in scores:
    if score >= 70:
        filtered.append(score)
print(filtered)

scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)
print(list(filtered))

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]
populated = filter(lambda c: c[1] > 300000000, countries)
print(list(populated))


print ("-----  List() and  Reduce (from impot functools)  ----  ")
scores = [75, 65, 80, 95, 50]
total = 0
for score in scores:
    total += score
print(total)


def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b
scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)

print ("-----  List comprehansion  ----  ")
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares)

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]
highest_mountains = [m for m in mountains if m[1] > 8600]
print(highest_mountains)