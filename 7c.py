# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:52:40 2020

@author: PC1
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

plt.style.use('default')


# data analysis example 3

file = Path('data') / 'dietpill.xlsx'
df = pd.read_excel(file, sheet_name='Sheet1')

print(df.head())
print(df.shape)


# calculate weight change
df['weight_change'] = df['weight_end'] - df['weight_start']

# by percent
df['change_pct'] = df['weight_change'] / df['weight_start'] * 100

# subset data
d1 = df.loc[df['group']=='control', 'weight_change']
d2 = df.loc[df['group']=='pill', 'weight_change']


# plot

f, ax = plt.subplots()
d1.hist(alpha=0.6, ax=ax, label='control')
d2.hist(alpha=0.6, ax=ax,  label='pill')
ax.legend()
ax.set_title('weight_change')


f, ax = plt.subplots()
df.boxplot(column=['weight_change'], by='group', ax=ax)
ax.grid(False)
f.suptitle(None)


plt.show()


# stats

from scipy.stats import normaltest, ttest_ind

print('-' * 20)
print('normality test:')
print('if p-val is very small, it means it is unlikely that the data ' + 
      'came from a normal distribution.')
print(normaltest(d1))
print(normaltest(d2))


print('-' * 20)
tstat, pval = ttest_ind(d1, d2)
print('ttest: stat {}, p-val {}'.format(tstat, pval))



