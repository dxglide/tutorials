##### https://www.pythontutorial.net/python-basics/python-string/


param1 = 10;
print("hello\n");
print(2*1.99);

# commetai cia 

# funnkijos pvz

def test_funckija(input1):
    """ Cia mano funckijos aparasymas """
    print("tomo funckija")
    print("kita funkcija")

    if (input1 == 1):
        print("Cia 1")
    else:
        print("visai kitas skaicius")

test_funckija(1)

print("---------------------------------------------------")

message = 'TESTAS: IT\'s "Beautiful is better than ugly.". Said Tim Peters'
raw_message = r'C:\python\bin'
multi_line_message = '''
kaip editorius
kitas eilute
trecia eil....
'''

print(message)
print('RAW MESSAGE ' + raw_message)
print(multi_line_message)

#variables in parameters ...
name = 'John'
message = f'Hi {name}'
print(message)

#concatating 
greeting = 'Good ' 'Morning!'
print(greeting)

greeting = 'Good '
time = 'Afternoon'
greeting = greeting + time + '!'
print(greeting)

# a string is a sequence of characters, you can access its elements using an index. The first character in the string has an index of zero.
print("\nString as array  ......")
str = "Python String"
print(str[0]) # P
print(str[1]) # y
print("Negative from string array ...")
print(str[-1])  # g
print(str[-2])  # n


# the lenght
#  

print("\nthe lenght ......")
str_len = len(str)
print(str_len)

print("\nSlicing - substrsing  ......")
print(str[0:2])

print("\n")
print("Sring manipulation  ......")
print("Original: " +  str)
str_modified = 'J' + str[1:]
str_modified = 'J' + str[1:]
print("str_modified : " +  str_modified)

print("\n")
print("Numbers ---------------\n")
# Python supports integers, floats, and complex numbers. This tutorial discusses only integers and floats.
# https://www.pythontutorial.net/python-basics/python-numbers/


print("\n")
print("Booleans ---------------\n")
# Note that the boolean values True and False start with the capital letters (T) and (F). 
is_active = True
is_admin = 0
if is_active == 1:
    print("is active")
else:
    print("is not active")

if is_admin == 1:
    print("is admin")
else:
    print("is not admin")

print(100>10)
print("To find out if a value is True or False, you use the bool() function.")
print("\n");
print(bool('Hi'))
print(bool(''))
print(bool(0))
print(bool(2))