
print("-------- Special methods  --------")
print("-------- __str__  --------")
# https://www.pythontutorial.net/python-oop/python-__str__/

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # __str__ method is a special method that returns a string representation of an object.    
    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'
    # __repr__ method is a special method that returns a string representation of an object.
    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'
    
person = Person('John', 'Doe', 25)
print(person)


print("-------- __repr__  --------")
# https://www.pythontutorial.net/python-oop/python-__repr__/
print(repr(person))  # Person("John","Doe",25)


print("-------- __eq__  --------")
# https://www.pythontutorial.net/python-oop/python-__eq__/


