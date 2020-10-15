# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:55:39 2020

@author: PC1
"""

# 3. fundamentals


# a. print

print('Hello')

# concatenation
print('H', 'e', 'l', 'l', 'o')

print('H' + 'e' + 'l' + 'l' + 'o')

print('H', 'e', 'l', 'l', 'o', sep='')


print(123)


# comment


# b. variables and data types

# string
print(type('hello'))

# special escape sequences
print('abc\tdef')  # tab
print('abc\ndef')  # new line

# raw strings: escape sequences not translated
print(r'abc\tdef')


a = 10  # integer
b = 20.5  # float

print(type(a))
print(type(b))

print('a + b =', a+b)
print(type(a+b))

# redefine variables
a1 = 5
b1 = a1
a1 = 6
print(a1, b1)


# type 
c = .43e6
print(c, type(c))

# maximum value of floating point number in python:
d1 = 1.797e308
print(d1)
d2 = 1.798e308
print(d2)
d3 = -1.797e308
print(d3)
d4 = -1.798e308
print(d4)

# complex number
z1 = 2 + 5j
print(z1, type(z1))
print('real part:', z1.real)
print('imaginary part:', z1.imag)


c = "1234567890"
print(c)

# create list from string (will talk about lists later)
d = list(c)
print(d)

# length of string
print(len(c))

# string characters
print(c[1], c[-1])

print(type(c))
print(type(d))

# range
print(c[0:5])

# with step size
print(c[0:8:2])

# method (function that belongs to a class)
print(c.find('4'))


# c. math operations
print(10 + 20)  # add
print(10 - 20)  # subtract
print(7 * 2)  # multiply
print(7 ** 2)  # exponentiate
print(7 / 2)  # divide (int)
print(7 / 2.)  # divide (float)
print(7 % 2)  # modulus (remainder)
print(7 // 2)  # floor divide


# boolean
# comparison operators: ==, !=, >, <, >=, <=
ans = (5 > 7)
print(type(ans))
print(ans)

ans2 = (5 <= 7)
print(ans2)

