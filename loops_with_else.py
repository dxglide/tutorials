# https://www.pythontutorial.net/python-basics/python-for-else/

# In Python, the for statement can have an optional else clause,
#  which you may not be familiar with especially if you’re coming from other languages such as Java or C#.

# The else clause in the for statement is executed when the loop completes normally.

# for item in iterables:
#     # process item 
# else:
#     # statement

# In this syntax, the else clause will execute only if the loop runs normally.
# In other words, the else clause won’t execute if the loop encounters a break statement.
# In addition, the else clause also executes when the iterables object has no item.

# people = [{'name': 'John', 'age': 25},
#         {'name': 'Jane', 'age': 22},
#         {'name': 'Peter', 'age': 30},
#         {'name': 'Jenifer', 'age': 28}]
# name = input('Enter a name:')

# found = False
# for person in people:
#     if person['name'] == name:
#         found = True
#         print(person)
#         break

# if not found:
#     print(f'{name} not found!')


people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = input('Enter a name:')

for person in people:
    if person['name'] == name:
        print(person)
        break
else:
    print(f'{name} not found!')


print ("----- WHILE WITH ELSE   ----  ")
# When the condition becomes False and the loop runs normally, the else clause will execute. 
# However, if the loop is terminated prematurely by either a break 
# or return statement, the else clause won’t execute at all.
basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

fruit = input('Enter a fruit:')

index = 0

while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item['fruit'] == fruit:
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        found_it = True
        break

    index += 1
else:
    qty = int(input(f'Enter the qty for {fruit}:'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)


print ("----- DO WHILE   WITH ELSE   ----  ")
#Unlike the while loop, the do...while loop statement executes at least one iteration. 
# It checks the condition at the end of each iteration and executes a code block until the condition is False.
# In Python, you can simulate the do...while loop using the while loop with the else clause.