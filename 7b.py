# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:32:36 2020

@author: PC1
"""

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(palette='colorblind', style='white')
plt.style.use('default')


# data analysis example 2


# https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita
# https://en.wikipedia.org/wiki/List_of_countries_by_traffic-related_death_rate
# https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate
file = Path('data') / 'alcohol_traffic_fatality.xlsx'
df1 = pd.read_excel(file, sheet_name='homicide')
df2 = pd.read_excel(file, sheet_name='traffic')

print(df1.head())
print(df1.shape)

print(df2.head())
print(df2.shape)


df = pd.merge(df1, df2, how='inner', on=['Country', 'Total', 
                                         'Recordedconsumption', 
                                         'Unrecordedconsumption'])


# visualize

top_homi = df.nlargest(8, 'Homicide_rate')
f, ax = plt.subplots()
sns.barplot(data=top_homi, y='Country', x='Homicide_rate', ax=ax)
#ax.xaxis.set_tick_params(rotation=45)
f.suptitle('Highest Homicidal Rate (per 100k residents)')

top_fatal = df.nlargest(8, 'fatal_per_100k_vehicles')
f, ax = plt.subplots()
sns.barplot(data=top_fatal, y='Country', x='fatal_per_100k_vehicles', ax=ax)
f.suptitle('Highest traffic fatality Rate (per 100k vehicles)')


f, ax = plt.subplots()
df.plot(kind='scatter', x='Total', y='Homicide_rate', ax=ax)
ax.set_title('Homicide rate vs Alcohol per capita')


f, ax = plt.subplots()
df.plot(kind='scatter', x='Total', y='fatal_per_100k_inhabitants_per_yr', ax=ax)
ax.set_title('Traffic fatality rate vs Alcohol per capita')

g = sns.lmplot(data=df, x='Total', y='fatal_per_100k_inhabitants_per_yr')


# annotate
g = sns.lmplot(data=df, x='Total', y='Homicide_rate', 
               aspect=1.4, markers='^', scatter_kws={'alpha': 0.5})
thai = df.loc[df['Country']=='Thailand', ['Total', 'Homicide_rate']]
g.ax.annotate('Thailand', xy=(thai['Total'], thai['Homicide_rate']))
max_drink_idx = df['Total'].idxmax()
max_homi_idx = df['Homicide_rate'].idxmax()
max_drink_ctry = df.loc[max_drink_idx, 'Country']
max_homi_ctry = df.loc[max_homi_idx, 'Country']
g.ax.annotate(max_drink_ctry, 
              xy=(df.loc[max_drink_idx, 'Total'], 
                  df.loc[max_drink_idx, 'Homicide_rate']))
g.ax.annotate(max_homi_ctry, 
              xy=(df.loc[max_homi_idx, 'Total'], 
                  df.loc[max_homi_idx, 'Homicide_rate']))


g = sns.lmplot(data=df, x='Total', y='fatal_per_100k_vehicles', 
               aspect=1.4, markers='^', scatter_kws={'alpha': 0.5})
thai = df.loc[df['Country']=='Thailand', ['Total', 'fatal_per_100k_vehicles']]
g.ax.annotate('Thailand', xy=(thai['Total'], thai['fatal_per_100k_vehicles']))
max_drink_idx = df['Total'].idxmax()
max_fatal_idx = df['fatal_per_100k_vehicles'].idxmax()
max_drink_ctry = df.loc[max_drink_idx, 'Country']
max_fatal_ctry = df.loc[max_fatal_idx, 'Country']
g.ax.annotate(max_drink_ctry, 
              xy=(df.loc[max_drink_idx, 'Total'], 
                  df.loc[max_drink_idx, 'fatal_per_100k_vehicles']))
g.ax.annotate(max_fatal_ctry, 
              xy=(df.loc[max_fatal_idx, 'Total'], 
                  df.loc[max_fatal_idx, 'fatal_per_100k_vehicles']))


g = sns.lmplot(data=df, x='Total', y='fatal_per_100k_inhabitants_per_yr', 
               aspect=1.4, markers='^', scatter_kws={'alpha': 0.5})
thai = df.loc[df['Country']=='Thailand', 
              ['Total', 'fatal_per_100k_inhabitants_per_yr']]
g.ax.annotate('Thailand', xy=(thai['Total'], 
                              thai['fatal_per_100k_inhabitants_per_yr']))
max_drink_idx = df['Total'].idxmax()
max_fatal_idx = df['fatal_per_100k_inhabitants_per_yr'].idxmax()
max_drink_ctry = df.loc[max_drink_idx, 'Country']
max_fatal_ctry = df.loc[max_fatal_idx, 'Country']
g.ax.annotate(max_drink_ctry, 
              xy=(df.loc[max_drink_idx, 'Total'], 
                  df.loc[max_drink_idx, 'fatal_per_100k_inhabitants_per_yr']))
g.ax.annotate(max_fatal_ctry, 
              xy=(df.loc[max_fatal_idx, 'Total'], 
                  df.loc[max_fatal_idx, 'fatal_per_100k_inhabitants_per_yr']))


f, ax = plt.subplots(nrows=3, figsize=(8, 9))
sns.boxplot(data=df, x='Continent', y='Total', ax=ax[0])
sns.boxplot(data=df, x='Continent', y='Homicide_rate', ax=ax[1])
sns.boxplot(data=df, x='Continent', y='fatal_per_100k_vehicles', ax=ax[2])
f.tight_layout()

plt.show()
