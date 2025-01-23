# https://www.pythontutorial.net/python-basics/python-module/
# https://www.pythontutorial.net/python-basics/python-module-search-path/
# https://www.pythontutorial.net/python-basics/python-__name__/ 


# A module is a piece of software that has a specific functionality.
#  A Python module is a file that contains Python code.
# For example, when building a shopping cart application,
#  you can have one module for calculating prices and another
#  module for managing items in the cart. Each module is a separate Python source code file.

# A module has a name specified by the filename without the .py extension. 
# For example, if you have a file called pricing.py, the module name is pricing


import pricing
import pricing as selling_price
from pricing import get_net_price

net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)
print(net_price)

net_price = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)


net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)


# Python will search for the module.py file from the following sources:

# The current folder from which the program executes.
# A list of folders specified in the PYTHONPATH environment variable, if you set it before.
# An installation-dependent list of folders that you configured when you installed Python.

# Python stores the resulting search path in the sys.path variable that comes from the sys module.

import sys

for path in sys.path:
    print(path)


#     To make sure Python can always find the module.py, you need to:

# Place module.py in the folder where the program will execute.
# Include the folder that contains the module.py in the PYTHONPATH environment variable. Or you can place the module.py in one of the folders included in the PYTHONPATH variable.
# Place the module.py in one of the installation-dependent folders.

# Runtime: 
# >>> import sys
# >>> sys.path.append('d:\\modules\\')
# >>> import recruitment
# >>> recruitment.hire()
# Hire a new employee...

print("----   Python __name__ ---- ")
# If you have gone through Python code, you’ve likely seen the __name__ variable like the following:

# if __name__ == '__main__':
#     main()


# Since the __name__ variable has double underscores at both sides,
#  it’s called dunder name. The dunder stands for double underscores

# The __name__ is a special variable in Python. It’s special
#  because Python assigns a different value to it depending on how its containing script executes.

# When you import a module, Python executes the file associated with the module.

# Often, you want to write a script that can be executed directly
#  or imported as a module. The __name__ variable allows you to do that.

# When you run the script directly, Python sets the __name__ variable to '__main__'.

# However, if you import a file as a module, Python sets the module name to the __name__ variable.


