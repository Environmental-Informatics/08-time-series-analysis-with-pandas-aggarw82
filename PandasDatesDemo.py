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

# load data
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')					
# print(ao)
# print('Rows, Columns:', ao.shape)

# Generate Dates
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')			
AO = Series(ao[:,2], index=dates)
# print('Dates:', dates.shape[0])
# print(AO)

# Generate Daily Atlantic Oscillation (AO) plot
AO.plot(title='AO plot')												
plt.ylabel('AO')
plt.xlabel('Year')
plt.savefig('Tut_[23]_AO_plot.png')
plt.close() 


''' Daily North Atlantic Oscillation (NAO) '''

# load data
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')				
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)
# print(NAO.index)

# creating a dataframe from both AO and NAO
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})								

# plotting both NAO and AO
# plt.figure	plt.savefig('Coeff_Var_both.png', dpi = 96)
	# plt.close() ()
# aonao.plot(subplots=True)
# plt.show()

# adding new column
aonao['Diff'] = aonao['AO'] - aonao['NAO']								
print(aonao.head())

# deleting column
del aonao['Diff']														
print(aonao.tail())


'''Statistical analysis of data frame'''

print('\nMean:\n',aonao.mean())
print('\nMax:\n',aonao.max())
print('\nMin:\n',aonao.min())
print('\nMean(1):\n',aonao.mean(1))
print('\nDescribe:\n',aonao.describe())


'''Resampling Median'''
AO_mm = AO.resample("A").median()
AO_mm.plot(title='Resampled Median')
plt.ylabel('AO_mm')
plt.xlabel('Year')
plt.savefig('Tut_[48]_AO_mm.png')
plt.close() 


'''Rolling Statistics'''
aonao.rolling(window=12, center=False).mean().plot(title='Rolling Mean', style='-g')
plt.ylabel('Rolling Mean')
plt.xlabel('Year')
plt.savefig('Tut_[52]_rolling_mean.png')
plt.close() 





