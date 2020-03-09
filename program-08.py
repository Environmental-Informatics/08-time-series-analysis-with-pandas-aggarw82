""" Program to read data from file, process it
    and draw graphs using matplotlib
    
    Appropriate titles should be given
    and axis should be labeled 

    Author: Varun Aggarwal
    Username: aggarw82
    Github: https://github.com/Environmental-Informatics/08-time-series-analysis-with-pandas-aggarw82
"""

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import numpy.random as random
import seaborn as sb
from statsmodels.graphics.gofplots import qqplot

# read file. Change file name for processing data from different date range
inFile = "all_month.csv"
data  = pd.read_csv(inFile,
					parse_dates=True, 
					header=0,
					warn_bad_lines=True)


mag = np.nan_to_num(data['mag']) #Converting NA values to 0

# Histogram with bin width=1
bins = [0,1,2,3,4,5,6,7,8,9,10]
fig = plt.hist(mag, bins=bins)
plt.title("Count of Earthquake Magnitude")
plt.xlabel("Magnitude")
plt.ylabel("Count")
plt.savefig('results_fig1.png')
plt.show()


# KDE plot: Kernel=Gaussian, Width=0.1
sb.kdeplot(mag,
		   shade=True,
		   kernel='gau',
		   bw=0.1,
		   legend=False,
		   clip=(0,11))
plt.xlim(0, 10)
plt.xlabel('Magnitude')
plt.ylabel('Density')
plt.title('KDE Plot of Magnitude')
plt.savefig('results_fig2.png')
plt.show()

# plot long and lat 
plt.plot(data['longitude'], data['latitude'], '*')
plt.xlim(-180,180) 									# set x and y limits to imitate world coordinates
plt.ylim(-90,90)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earthquake Location')
plt.savefig('results_fig3.png')
plt.show()

# plot the cumulative histogram by setting cumulative flag as True
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(data['depth'], 1000, 
		density=True,
		histtype='stepfilled',
       	cumulative=True)
ax.grid(True)
ax.set_title('Normalized CDF of Earthquake Depth')
ax.set_xlabel('Depth')
ax.set_ylabel('Likelihood of occurrence')
plt.savefig('results_fig4.png')
plt.show()


# Generate scatter plot of Magnitude and Depth
plt.scatter(data['mag'], 
			data['depth'], 
			marker='.')
plt.xlabel('Magnitude')
plt.ylabel('Depth')
plt.title('Depth vs. Magnitude of EarthQuakes')
plt.savefig('results_fig5.png')
plt.show()

# Generate QQ  plot
qqplot(data['mag'], line ='s')
plt.title('QQ Plot')
plt.savefig('results_fig6.png')
plt.show()