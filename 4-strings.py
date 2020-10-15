# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:06:49 2020

@author: PC1
"""

# 4. strings

# a. formatting

print('A')
print()  # empty line
print('B'*5)  # multiple characters
print('C'+' '+'D'+' '+str(10))
print('C'+' '+'D', 10)  # commas are used in functions and arrays
print('AAA', 'BBB', end=',')  # use other character instead of newline ('\n')
print('CCC')
print('AAA', 'BBB', 'CCC', sep=',', end='\n')  # specify separator
print('AAA', '&' * 10, 'BBB', sep='--', end='\n')  # specify separator

print('Number: ' + str(1000) + ' ' + str(55.55))
print('Number:', 1000, 55.55)
print('Number: %i %f' % (1000, 55.55))  # int and float
print('Number: %i %.2f' % (1000, 55.55))  # specify decimal place)
print('Number: %8i %0.2f' % (1000, 55.55))  # specify size
print('Number: %08i %0.2f' % (1000, 55.55))  # fill in zeros
print('Number: %08i %8.2f' % (1000, 55.55))
print('{:s}: {:d} {:f}'.format('Number', 1000, 55.55))
a, b = 1000, 55.55
print(f'Number: {a} {b:.2f}')
print('String: %c' % ('T'))
print('String: %s' % ('Thai'))


a = 12345.6789
print('Number {:f}'.format(a))
print('Number {:0,f}'.format(a))  # add thousand comma (for display)
print('Number {:,.3f}'.format(a))  # specify decimal place
print('Number {:12,.3f}'.format(a))  # specify size
b, c = 111.11, 222.22
print('Number {0}, {1:0,f}, {2:,.3f}'.format(a, b, c))  # 0, 1, 2 = order

t = '{0:12,.3f}'  # use variable for format
print('Number:', t.format(a))
print('Number:', t.format(b))


print('-' * 30)


# b. operations

s = 'thai@mail.com'
print(s)
print(len(s))  # length function
print(s.index('@'))  # get index (location)
print(s.count('i'))  # get count
print(s.split('@'))
print(s.split('@')[0])
# several ways to get 'mail'
print(s[5:9])
print(s.split('@')[-1].split('.')[0])
print(s[s.find('mail'):s.find('mail')+len('mail')])

s2 = 'thai524262q6@mail.com'
print(s2)
print(s2[0:s2.find('@')])  # get name
print(s2.count('a'))  # count 'a'

# string operations
print(' '.join(['cOFFeE', 'Break']))
print('cOFFeE'.upper())
print('cOFFeE'.lower())
print('cOFFeE'.title())
print('cOFFeE'.lower().replace('f','x').replace('e','a'))


s = '   abc   def   '
print(s)
print(len(s))
# cleansing
print(s.strip())  # strip spaces at begin and end
print(len(s.strip()))
print(s.rstrip())  # strip spaces at end
print(s.lstrip())  # strip spaces at begin
print(s.replace(' ', ''))  # remove all spaces

print('-' * 20)
s2 = '   abc   def   \t\r\n'  # tab, return, newline
print(s2)
print(len(s2))
print(s2.strip())
print(len(s2.strip()))


t = '11,22,33,44'
print(t)
ts = t.split(',')
print(ts)
print(list(map(int,ts)))
s = '###'.join(ts)
print(s)


s = 'Thailand Institute of Nuclear Technology (Public Organization)'
print(s)
print(s.lower())
name = s.split('(')[0].strip().upper()
print(name)
first_letters = list(map(lambda s: s[0], name.split()))
print(first_letters)
first_letters.remove('O')
print(first_letters)
print(''.join(first_letters))

print(name[-1::-1])
