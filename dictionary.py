# A Python dictionary is a collection of key-value pairs where each key is associated with a value
# A value in the key-value pair can be a number, a string, a list, a tuple, 
# or even another dictionary. In fact, you can use a value of any 
# valid type in Python as the value in the key-value pair.
# A key in the key-value pair must be immutable. In other words, 
# the key cannot be changed, for example, a number, a string, a tuple, etc.

# Python uses curly braces {} to define a dictionary. 
# Inside the curly braces, you can place zero, one, or many key-value pairs.
# The following example defines an empty dictionary:
# empty_dict = {}

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person['first_name'])
print(person['last_name'])

# ssn = person['ssn']  invokes errror KeyError: 'ssn'

#workaround
ssn = person.get('ssn')
print(ssn)

ssn = person.get('ssn', '000-00-0000') # default value
print(ssn)


person['gender'] = 'Famale' # add new key-value pair
print(person)
person['age'] = 26 # modify the value of the key 'age'
print(person) 
del person['active'] # remove the key 'active'
print(person)

print(person.items())  # loop over dicatinar items
for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(key)
for value in person.values():
    print(value)

# https://www.pythontutorial.net/python-basics/python-dictionary-comprehension/
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}
print(new_stocks)

selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}
print(selected_stocks)