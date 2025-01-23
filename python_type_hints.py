# https://www.pythontutorial.net/python-basics/python-type-hints/

def say_hi(name: str) -> str:
    return f'Hi {name}'


greeting = say_hi('John')
print(greeting)

greeting = say_hi(False)
print(greeting)


# To check the syntax for type hints, you need to use a static type checker tool.
# Using a static type checker tool: mypy