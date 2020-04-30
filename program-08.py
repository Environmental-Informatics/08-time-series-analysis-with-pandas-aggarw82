""" Program to read data from file, process it
    and draw graphs using matplotlib
    
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

'''read file. Specify date column in parse_dates'''
inFile = "WabashRiver_DailyDischarge_20150317-20160324.txt"
data  = pd.read_csv(inFile,
					sep='\t',
					parse_dates=['datetime'],
					index_col=['datetime'],
					header=24,
					skiprows=[25],
					warn_bad_lines=True)
# print(data.head())

'''convert to time series''' 
data = Series(data['01_00060'])
# print(data.head())

'''re-sample for daily average'''
daily_avg = data.resample("D").mean()
daily_avg.plot(title = 'Daily Avg Discharge')
plt.xlabel('Date')
plt.ylabel('Discharge (cu ft/s)')
plt.savefig('Daily Avg Discharge.pdf')
plt.show()

'''10 highest discharge days'''
highest = daily_avg.sort_values(ascending=False)[:10]
highest.plot(title = 'Top 10 Highest Discharge', style='--o')
plt.xlabel('Date')
plt.ylabel('Discharge (cu ft/s)')
plt.savefig('Top 10 Discharge.pdf')
plt.show()

'''re-sample for monthly average'''
monthly_avg = data.resample("M").mean()
monthly_avg.plot(title = 'Monthly Avg Discharge', style='--o')
plt.xlabel('Date')
plt.ylabel('Discharge (cu ft/s)')
plt.savefig('Monthly Avg Discharge.pdf')
plt.show()