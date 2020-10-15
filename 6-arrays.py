# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:53:13 2020

@author: PC1
"""

# 6. arrays

# list
a = [602, 242, 689, 185, 800]

print(a)
print(len(a))
print(a[-1])  # last item
print(a[1:3])
print(sorted(a))  # function to sort values (a.sort() will sort in place)
print(sorted(a, reverse=True))
a.append('44')  # array can contain multiple data types
print(a)

a.remove(185)  # remove by value
print(a)

a.pop()  # remove the last item
print(a)

a.pop(1)  # remove second item
print(a)

a.clear()  # remove every item
print(a)


# extending list
a = [1, 2, 3]
b = [4, 5]
print(a)
print(b)
a.extend(b)
print(a)


# array types

a = ['proton', 'neutron', 'electron']  # list
b = {'proton', 'neutron', 'electron', 'neutron'}  # set (can't have duplicates)
c = ('proton', 'neutron', 'electron')  # tuple (can't be changed)

print(a, type(a))
print(b, type(b))
print(c, type(c))

# iterate
for i in range(len(a)):
    print(a[i])
    
# much more readable this way:
for x in a:
    print(x)
    
# convert array types
a2 = set(a)
print(a2)
b2 = tuple(b)
print(b2)
c2 = list(c)
print(c2)

# list of lists
d = [a, b, c]
print(d)

# immutable vs mutable
a = [1, 2, 3]
c = (1, 2, 3)
print('a =', a, type(a))
print('c =', c, type(c))

try:
    del a[0]
    print(a)
except:
    print('error')
    
try:
    del c[0]
except:
    print('error')


# zipping lists

first_names = ['Michael', 'Steph', 'LeBron', 'James']
last_names = ['Jordan', 'Curry', 'James', 'Harden']
for f, l in zip(first_names, last_names):
    print(' '.join([f, l]))
    
shapes = ['circle', 'rectangle', 'triangle', 'hexagon']
sides = [1, 4, 3, 6]
sum_angles = [360, 360, 180, 360]
for shape, side, sum_angle in zip(shapes, sides, sum_angles):
    print(shape, side, sum_angle)
    
    
# set operations

a = {1, 2, 3, 4}
b = {3, 4, 7, 9, 11}
print(len(a) == len(b))
print('a=', a)
print('b=', b)

print(a | b)  # union (by operator)
print(a.union(b))  # union (by method)
print(a & b)  # intersect
print(a.intersection(b))  # intersect
print(a - b)
print(a.difference(b))
print(a ^ b)
print(a.symmetric_difference(b))


# dictionary

d1 = {'year': 2006, 'city': 'Bangkok', 'division': 'R&D'}
print(d1['year'])
print(d1['city'])

print('print key-value pairs:')
for key, value in d1.items():
    print(key, value)
    
print('print keys only:')
for i in d1:
    print(i)
    
print('print values only:')
for i in d1.values():
    print(i)
    
    
# exercise: find discount

a = int(1e4)  # amount
t = 'B'  # types

# use dict instead of if-else to increase readability

# type-dependate discount rates
rates = {'A': 30, 'B': 20, 'C': 10}

# calculate discount
disc = rates[t]/100. * a

print(f'discount = {disc}')


list_1 = [101, 'thai', 1000]
print(list_1)

list_2 = [[1, 2, 3], [3, 4, 5]]
print(list_2)

list_3 = [{'id': 101, 'name': 'Batman'}, {'id': 102, 'name': 'Robin'}]
print(list_3)

dict_1 = {'id': 101, 'name': 'Rutherford', 'total': 1000}
print(dict_1)

dict_2 = {'id': [101, 102], 'name': ['Rutherford', 'Chadwick'], 
          'total': [1000, 1200]}
print(dict_2)

dict_3 = {'row1': {'a': [2, 5], 'b': [3, 4]}, 
          'row2': {'c': [4, 7], 'd': [1, 9]}}
print(dict_3)


# exercise

a = [['gamma', 'alpha', 'beta'], ['electron', 'xray', 'neutron']]

# get 2nd row
print(a[1])

# get last column
print([b[-1] for b in a])

# get electron
print(a[1][0])


# exercise

list_3 = [{'id': 101, 'name': 'Batman'}, {'id': 102, 'name': 'Robin'}]

# get Batman
print(list_3[0]['name'])


# exercise

isotopes = [{'name': 'oxygen 16',  'symbol': 'O', 'Z': 8, 'N': 8}, 
            {'name': 'carbon 14', 'symbol': 'C', 'Z': 6, 'N': 8}, 
            {'name': 'helium 4', 'symbol': 'He', 'Z': 2, 'N': 2}]

# get second isotope info
for k, v in isotopes[1].items():
    print('{} = {}'.format(k, v), end=', ')