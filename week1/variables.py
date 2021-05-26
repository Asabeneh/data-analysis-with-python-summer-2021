# What is variables ?
# Data types
# Operators
# Conditionals
# lIST
# lOOP
# SET 
# TUPLES
# DICTIONARY
# FUNCTIONS

## Numbers
a = 1
b = 2
total = a + b
print(total)

gravity = 9.81
mass = 75
weight = mass * gravity

print(weight)

radius = 10

area = 3.14 * radius ** 2

print(area)

# Data types: numbers(Integers, float, complex), 
# string, booleans, list, set, tuple, dictionary, None

print(type (9.81))
print(type(10))
print(type('Asabeneh'))
print(type(True))
print(type(False))
print(type(2 > 1))
print(type([1, 2, 3]))
print(type({1, 2, 3, 4}))
print(type((1, 2, 3, 4, 5)))
print(type({'kirja':'book','koulu':'school'}))
print(type(1 +2j))

# Booleans
print(True)
print(False)

# String

first_name = 'Asabeneh'
last_name = 'Yetayeh'

full_name = first_name + ' ' + last_name
print(full_name)

## methods of String
# uppper, lower, title
print(first_name)
print(first_name.upper())
print(first_name.lower())
print('i love PythoN'.title())
print(first_name.swapcase())

language = 'I love Python'
print(language.split())
programming_lang = 'python, R, matlab, and Java'
print(programming_lang.split(','))
print(' I love Python. '.strip())

# Operators: Arithmetic operators, Comparsions, logical operator

print(1 > 2)
print(2 >= 1)
print(1 < 2)
print(1 <= 2)
print(1 == 1)
print(1 != 1)
print(1 == '1')
print(2 == 'two')
print(1 is 1)
print(1 is not 2)
print(1 is 2)

# and or not
print(2 < 5 and 1 > 0)
print(2 < 5 and 1 < 0)
print(2 > 5 and 1 < 0)

print(2 < 5 or 1 > 0)
print(2 < 5 or 1 < 0 )
print(2 > 5 or 1 < 0)
print(not not 2 > 1)
