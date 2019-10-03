# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
## Variables
# x = 1           # int
# y = 2.5         # float
# name = 'John'   # string
# is_cool = True  # boolean

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math
a = x + y

# Console log of python
print(x, y, name, is_cool, a)

# Console log wich type x is
print(type(x))

# Casting - turn variable into string
x = str(x)
