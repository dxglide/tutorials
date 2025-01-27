# https://www.pythontutorial.net/python-oop/
# https://www.pythontutorial.net/python-oop/python-object-oriented-programming/


class Person:
    counter = 0  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def say_hello(self):
        print(f'Hello, my name is {self.name}')

    @classmethod  # class method ... cls is the class itself
    def create_anonymous(cls):
        return Person('Anonymous', 22)


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


person = Person('Tomas', 999)

print(person)  # <__main__.Person object at 0x000001E3D3D3A4C0>
print(type(person))  # <class '__main__.Person'>
print(isinstance(person, Person))  # True
print(callable(Person))  # True

def fn_is_callable():
    print("I'm callable")
print(callable(fn_is_callable))  # if cuntions is callbale

print("-------- Add attibutes and methodes  to a class --------")
person.name = 'John' # Add an attribute to the person object in runtime
print(person.name)  # John

another_person = Person('Tomas', 999)
print(another_person.name)
another_person.say_hello()
print(Person.counter)  # 2 # class attribute as static variable


anonymous = Person.create_anonymous()
print(anonymous.name)  # Anonymous
print(anonymous.age)  # 22
print(Person.counter)  # 2 # class attribute as static variable

print("-------- Static method  --------")
f = TemperatureConverter.celsius_to_fahrenheit(30)
print(f)  # 86


print("-------- Single inheritance  --------")
# Single inheritance
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    
    def say_hello(self):
        return str(super().say_hello()) + f" I'm a {self.job_title}."
    
employee = Employee('JohnX', 25, 'Python Developer')
print(employee.name)
# employee.say_hello()
print(employee.say_hello())