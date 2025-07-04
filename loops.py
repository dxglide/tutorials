# TETSING LOOPS IN PYTHON
("----- FOR LOOP ----- ")
for i  in range(10):
    print(i)
print ("-----------------")
for i  in range(5,10):
    print(i)

print ("-----------------")

for i  in range(5,20,3):
    print(i)
print ("-----------------")
suma = 0
for i  in range(5,20,3):
    suma += i
print(suma)


print("----- WHILE  LOOP ----- ")
max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1

print("----- LOOP BREAK ----- ")

for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})")


print("----- LOOP CONTINUE ----- ")
for index in range(10):
    if index % 2:
        continue

    print(index)

print("-----  IF STATEMENT  BY PASS ----- ")
counter = 1
max = 10
if counter <= max:
    counter += 1
else:
    pass   # the pass statement is a statement that does nothing. It’s just a placeholder for the code that you’ll write in the future.

print ("------ input echo while -----------")
command = ''

while command.lower() != 'q':
    command = input('>')
    print(f"Echo: {command}")