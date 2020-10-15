# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:22:51 2020

@author: PC1
"""

# 7. data analysis

# concept: 
# obtain, tidy, explore, analyze (OTEA)
# separate raw data from analysis


# a. reading data files (pandas)
import pandas as pd
# pd is a nickname. like calling Mr. Jonathan Gatogato as Jon


# Penguin size, clutch and blood isotope data for foraging adults 
# near Palmer Station, Antarctica
file = 'data/penguins_lter.csv'

# read data into dataframe
df = pd.read_csv(file)  

print(df.head())

print(df.shape)

print(df.columns)

print(df.isna().sum())

# cleaning
df = df.drop(columns=['Comments'])

# filtering data
female_isotopes = df.loc[df['Sex']=='FEMALE', 
                         ['Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']]
print(female_isotopes.sample(10))


# b. statistical summary
from scipy.stats import skew, kurtosis, zscore
import numpy as np
from scipy import stats


print(df['Island'].value_counts())

print(df.describe())


avg_mass = df['Body Mass (g)'].mean()
sd_mass = df['Body Mass (g)'].std()
print('mean = {}, sd = {}'.format(avg_mass, sd_mass))

masses = df['Body Mass (g)'].dropna().values
print(len(masses))
print('median: {}, mode: {}'.format(np.median(masses), stats.mode(masses)))


print('-' * 20)
vals_flipper = df['Flipper Length (mm)'].dropna().values

print('Flipper length distribution characteristics:')
print('skewness (symmetry):', skew(vals_flipper))  # 0 for norm dist
print('kurtosis (tailness):', kurtosis(vals_flipper))  # 3 for norm dist


zscores_flipper = zscore(vals_flipper)

for flip, z in zip(vals_flipper[:5], zscores_flipper[:5]):
    print(flip, z)


# c. visualization
import matplotlib.pyplot as plt

plt.style.use('default')


vars_plot = ['Culmen Length (mm)', 'Culmen Depth (mm)', 
             'Flipper Length (mm)', 'Body Mass (g)']

plt.figure()
df[vars_plot].hist()

plt.figure()
plt.hist(df['Culmen Length (mm)'].dropna(), bins=30)
plt.title('culmen length')


plt.figure()
plt.hist(zscores_flipper, bins=30)
plt.title('z-score distribution of flipper length')


plt.figure()
plt.scatter(df['Culmen Length (mm)'], df['Culmen Depth (mm)'])
plt.xlabel('Culment Length (mm)')
plt.ylabel('Culment Depth (mm)')

plt.show()


plt.figure()
plt.scatter(df.loc[df['Island']=='Biscoe', 'Culmen Length (mm)'], 
            df.loc[df['Island']=='Biscoe', 'Culmen Depth (mm)'], 
            marker='$\clubsuit$', label='Biscoe')
plt.scatter(df.loc[df['Island']=='Dream', 'Culmen Length (mm)'], 
            df.loc[df['Island']=='Dream', 'Culmen Depth (mm)'], 
            marker='$\spadesuit$', label='Dream')
plt.scatter(df.loc[df['Island']=='Torgersen', 'Culmen Length (mm)'], 
            df.loc[df['Island']=='Torgersen', 'Culmen Depth (mm)'], 
            marker='$\heartsuit$', label='Torgersen')
plt.legend()
plt.xlabel('Culment Length (mm)')
plt.ylabel('Culment Depth (mm)')


markers = ['o', 'd', '>']
f, ax = plt.subplots()
for sp, mk in zip(df['Species'].unique(), markers):
    d = df.loc[df['Species']==sp, ['Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']]
    ax.scatter(d['Delta 15 N (o/oo)'], d['Delta 13 C (o/oo)'], 
                 marker=mk, label=sp)
ax.set(xlabel='Delta 15 N', ylabel='Delta 13 C')
ax.legend()

plt.show()


# d. correlation test
from scipy.stats import pearsonr, normaltest
from scipy.stats.mstats import spearmanr

# find linear correlation between two data groups
# requirement: both groups are normally distributed


d = df[['Flipper Length (mm)', 'Culmen Length (mm)']].dropna()
d1 = d['Flipper Length (mm)']
d2 = d['Culmen Length (mm)']

plt.figure()
plt.scatter(d1, d2)
plt.xlabel('Flipper Length')
plt.ylabel('Culmen Length')

plt.show()


print('normality test:')
print('if p-val is very small, it means it is unlikely that the data ' + 
      'came from a normal distribution.')

# check shape
plt.figure()
plt.hist(d1)

plt.figure()
plt.hist(d2)

plt.show()

print(normaltest(d1))
print(normaltest(d2))


r, p = pearsonr(d1, d2)
print('Pearson correlation coeff: {}, p-value: {}'.format(r, p))

r, p = spearmanr(d1, d2)
print('Spearman correlation coeff: {}, p-value: {}'.format(r, p))


print('-' * 30)


# e. compare distribution
from scipy.stats import ttest_ind

# t-test requirement: independent samples with identical variances


# compare samples
def do_ttest(dat1, dat2, name1, name2, alpha=0.05):
    print('-' * 20)
    print('t-test: a two-sided test for the null hypothesis that 2 '
          'independent samples have identical average (expected) values.')
    print('-' * 20)
    print('{} vs {}'.format(name1, name2))
    stat, pval = ttest_ind(dat1, dat2)

    # interpret
    print('t-stat: {:.3f}, p-value: {:.3g}'.format(stat, pval))
    if pval > alpha:
        print('conclusion: same distributions (fail to reject H0)')
    else:
        print('conclusion: different distributions (reject H0)') 


d = df[['Island', 'Body Mass (g)']].dropna()
d1 = d.loc[df['Island']=='Biscoe', 'Body Mass (g)']
d2 = d.loc[df['Island']=='Dream', 'Body Mass (g)']
print('variances: d1: {}, d2: {}'.format(np.var(d1), np.var(d2)))
do_ttest(d1, d2, 'Biscoe island', 'Dream island')


d1 = d.loc[df['Island']=='Biscoe', 'Body Mass (g)']
d2 = d.loc[df['Island']=='Torgersen', 'Body Mass (g)']
print('variances: d1: {}, d2: {}'.format(np.var(d1), np.var(d2)))
do_ttest(d1, d2, 'Biscoe island', 'Torgersen island')


# f. PCA and LDA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA


features = ['Culmen Length (mm)', 'Culmen Depth (mm)', 
            'Flipper Length (mm)', 'Body Mass (g)', 'Sex', 
            'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']
target = 'Species'

d = df.loc[:, features + [target]]
d.dropna(inplace=True)

x = d[features].copy()
y = d[target].copy()

x = pd.get_dummies(x, drop_first=True)

scaler = StandardScaler()
x = scaler.fit_transform(x)

labenc = LabelEncoder()
labenc.fit(y)
y_enc = labenc.transform(y)
labels = labenc.classes_


def get_x_lda(x, y, n_components):
    lda = LinearDiscriminantAnalysis(n_components=n_components)
    lda.fit(x, y)
    x_reduced = lda.transform(x)
    # Percentage of variance explained for each components
    print('explained variance ratio:', lda.explained_variance_ratio_, 
          'sum:', lda.explained_variance_ratio_.sum())
    return x_reduced


def get_x_pca(x, n_components):
    pca = PCA(n_components=n_components)
    pca.fit(x)
    x_reduced = pca.transform(x)
    print('explained variance ratio:', pca.explained_variance_ratio_, 
          'sum:', pca.explained_variance_ratio_.sum())
    return x_reduced


n_components = 2

x_pca = get_x_pca(x, 2)
x_lda = get_x_lda(x, y_enc, 2)


def plot2components2(x, y, colors, size, label_names, title='title', 
                     xlabel='x1', ylabel='x2'):
    '''plot using colors and showing labels'''
    fig, ax = plt.subplots(dpi=100)
    for i, label_name in enumerate(label_names):
        print(i, label_name)
        ax.scatter(x[y==label_name, 0], x[y==label_name, 1], c=colors[i], 
                   s=size, alpha=0.5, label=label_name)
    ax.legend(framealpha=0.4, bbox_to_anchor=(1.05, 1))
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
#    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    fig.tight_layout()
    
    
plot2components2(x_pca, y, ['b', 'r', 'g'], 20, labels, title='PCA', 
                 xlabel='x1', ylabel='x2')

plot2components2(x_lda, y, ['b', 'r', 'g'], 20, labels, title='LDA', 
                 xlabel='x1', ylabel='x2')