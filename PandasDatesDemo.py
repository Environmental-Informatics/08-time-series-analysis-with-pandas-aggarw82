""" Program to read data from file, process it
    and draw graphs using Pa
    
    Appropriate titles should be given
    and axis should be labeled 

    Author: Varun Aggarwal
    Username: aggarw82
    Github: https://github.com/Environmental-Informatics/08-time-series-analysis-with-pandas-aggarw82
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',15) # this limit maximum numbers of rows

# pandas version
print('Pandas Version:', pd.__version__)


''' Daily Atlantic Oscillation (AO) '''


ao = np.loadtxt('monthly.ao.index.b50.current.ascii')					# load data
# print(ao)
# print('Rows, Columns:', ao.shape)


dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')			# Generate Dates
AO = Series(ao[:,2], index=dates)
# print('Dates:', dates.shape[0])
# print(AO)


AO.plot(title='AO plot')												# Generate Daily Atlantic Oscillation (AO) plot
plt.ylabel('AO')
plt.xlabel('Year')
plt.show()
# AO['1980-05':'1981-03'].plot()
# AO['1980':'1990'].plot()
# print(AO['1960'])




''' Daily North Atlantic Oscillation (NAO) '''


nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')				# load data
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)
# print(NAO.index)

	
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})								# creating a dataframe from both AO and NAO
# print(aonao)

# plotting both NAO and AO
# plt.figure()
# aonao.plot(subplots=True)
# plt.show()


aonao['Diff'] = aonao['AO'] - aonao['NAO']								# adding new column
print(aonao.head())


del aonao['Diff']														# deleting column
print(aonao.tail())


'''Statistical analysis of data frame'''

print('\nMean:\n',aonao.mean())
print('\nMax:\n',aonao.max())
print('\nMin:\n',aonao.min())
print('\nMean(1):\n',aonao.mean(1))
print('\nDescribe:\n',aonao.describe())


# Resampling Mean
# AO_mm = AO.resample("A").mean()
# plt.figure()
# AO_mm.plot(style='g--')
# plt.show()


'''Resampling Median'''
AO_mm = AO.resample("A").median()
AO_mm.plot(title='Resampled Median')
plt.ylabel('AO_mm')
plt.xlabel('Year')
plt.show()

# Resampling multiple plots
# AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
# AO_mm['1900':'2020'].plot(subplots=True)
# plt.show()
# AO_mm['1900':'2020'].plot()
# plt.show()
# print(AO_mm)

'''Rolling Statistics'''
aonao.rolling(window=12, center=False).mean().plot(title='Rolling Mean', style='-')
plt.ylabel('Rolling Mean')
plt.xlabel('Year')
plt.show()





