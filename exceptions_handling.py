# https://www.pythontutorial.net/python-basics/python-try-except/
# https://www.pythontutorial.net/python-basics/python-try-except-finally/
# https://www.pythontutorial.net/python-basics/python-try-except-else/

# n Python, errors that occur during the execution are called exceptions. The causes of exceptions mainly come from the environment where the code executes. For example:

# Reading a file that doesn’t exist.
# Connecting to a remote server that is offline.
# Bad user inputs.
# When an exception occurs, the program doesn’t handle it automatically. This results in an error message.

# In Python, exceptions have different types such as TypeError, NameError, etc.


# The try...except statement works as follows:

# The statements in the try clause execute first.
# If no exception occurs, the except clause is skipped and the execution of the try statement is completed.
# If an exception occurs at any statement in the try clause, the rest of the clause is skipped and the except clause is executed.

# try:
#     # code that may cause error
# except:
#     # handle errors


# try:
#     # code that may cause an exception
# except ValueError as error:
#     # code to handle the exception


# try:
#     # code that may cause an exception
# except Exception1 as e1:
#     # handle exception
# except Exception2 as e2:
#     # handle exception
# except Exception3 as e3:
#     # handle exception 



# try:
#     # code that may cause an exception
# except (Exception1, Exception2):
#     # handle exception



try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
except Exception as error:
    print(error)