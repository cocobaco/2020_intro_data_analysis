# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:08:06 2020

@author: PC1
"""

get_user_input = False


# 5. functions


# Functions are used to reduce redundancy

# example: find final concentration of two solutions of the same type at different conc
# A: 20% conc for 200 ml
# B: 45% conc for 120 ml

# define variables
conc_a = 20
vol_a = 100
conc_b = 25
vol_b = 120

# final conc = final quantity / final volume
# find final quantity
quan_final = (conc_a / 100) * vol_a + (conc_b / 100) * vol_b
# find final volume
vol_final = vol_a + vol_b

conc_final = quan_final / vol_final * 100
print('final concentration (%):', conc_final)

print('-' * 20)

# find final conc of C + D:
# C: 30% conc for 300 ml
# D: 60% conc for 100 ml
# ... repeat ...


# finding final solution concentration
def get_final_conc(conc_a, vol_a, conc_b, vol_b):
    quan_final = (conc_a / 100) * vol_a + (conc_b / 100) * vol_b
    vol_final = vol_a + vol_b    
    conc_final = quan_final / vol_final * 100
    print('final concentration (%):', conc_final)   
        

get_final_conc(20, 100, 25, 120)
get_final_conc(30, 300, 60, 100)


# global vs local variables

a = 100  # global
b = 20  # global


def func_print1(a):
    b = 100  # local b
    print(a)
    print(b)
    print(a * b)
    

func_print1(40)  # local a

print(a)  # global a
print(b)  # global b
print(a * b)


def func_print2(b):
    global a
    print(a)
    print(b)
    print(a * b)


func_print2(20)


# define functions

def sayhi(person):
    print('Hello {}, how are you?'.format(person))


def func_lazy(x):
    # this function does nothing
    pass


def function1(x):
    # this function doest something but returns nothing
    print('test function1', x)
    
    
def function2(x):
    ans = x * 5
    print('test function2', x)
    # this function returns something
    return ans


def function3(x1, x2):
    ans = x1 * 3 - x2 * 4
    print('test function3', ans)
    return ans


sayhi('Ann')
sayhi('Bob')

func_lazy(1000)
func_lazy(10)


function1('a')
function2('a')  # not storing output
function1(function2('a'))  # using one function's output as another's input
function3(4, -2)  # multiple arguments

function4 = lambda a: a * 7  # lambda function = anonymous, adhoc
print(function4(5))


# exercise 1: calculate sale price
a = 10000  # full price
sale = 0.1 * a  # 10% discount
net = a - sale  # final sale price
print('amount = {}, sale = {}, net = {}'.format(a, sale, net))


# define function
def calc_price(a, pct_disc):
    disc = (pct_disc/100.) * a  # 10% discount
    net = a - disc  # final sale price
    print('amount = {}, discount = {}, net = {}'.format(a, disc, net))
    

def get_inputs_price():
    a, d = 0, 0
    while a <= 0 or d <= 0 or d > 100:
        a = float(input('amount: '))
        d = float(input('discount %: '))
    return a, d


calc_price(100000, 10)  # use fixed inputs

if get_user_input:
    # get user input
    a, d = get_inputs_price()
    calc_price(a, d)  # pass inputs into function


# positional vs keyword arguments
def func4(a, b, c):
    print(a, b, c)


func4(1, 2, 3)  # using position

func4(a=2, b=3, c=1)  # using keywords


# one can set default values, making the terms optional
def func5(a, b, c=0):
    print(a, b, c)
    

func5(a=8, b=9)


# exercise 2: calculate mortgage monthly payment
# https://en.wikipedia.org/wiki/Mortgage_calculator
def calc_mortgage(price, interest_ann, years):
    print('=== Mortgage Calculator ===')
    print('price = {}, annual interest = {}%'.format(price, interest_ann))
    months = 12 * years
    
    if interest_ann > 0:
        r_mo = interest_ann / 12. / 100.
        # full_price = price * (1 + (interest_mo/100.)) ** months
        monthly_payment = price * r_mo / (1 - (1+r_mo)**(-months))
        full_price = monthly_payment * months
    else:
        monthly_payment = price / months
        full_price = price
        
    print('monthly payments: {:,.2f} for {} years ({} months)'\
          .format(monthly_payment, years, months))
    print('full price: {:,.2f}'.format(full_price))
    
    
def get_inputs_mortgate():
    price, interest, years = 0, 0, 0
    while price <= 0 or interest <= 0 or years <= 0:
        price = float(input('house price: '))
        interest = float(input('annual interest (%): '))
        years = int(input('years: '))
    return price, interest, years


calc_mortgage(10000, 0, 10)  # no interest

calc_mortgage(10000, 8, 10)


if get_user_input:
    price, interest, years = get_inputs_mortgate()
    calc_mortgage(price, interest, years)


