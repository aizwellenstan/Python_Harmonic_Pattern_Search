import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
from harmonic_functions import *

# Import historical data

# data = pd.read_csv('Data/JP225_D1.csv')
data = pd.read_csv('Data/JP225_H1.csv')
# data = pd.read_csv('Data/USDJPY_D1.csv')
# data = pd.read_csv('Data/USDJPY_H1.csv')

# data.columns = [['LocalTime', 'open', 'high', 'low', 'close', 'vol']]
data.columns = [c.strip().lower().replace(' ','_') for c in data.columns]

# data.Date = pd.to_datetime(data.Date, format='%d.%m.%Y %H:%M:%S.%f')

data = data.set_index(data.local_time)

data = data[['open','high','low','close','volume']]

data = data.drop_duplicates(keep=False)

price = data.close.iloc[:9000]


# Fubd our relative extrema

### v1
# max_idx = argrelextrema(price.values, np.greater, order=1)
# min_idx = argrelextrema(price.values, np.less, order=1)
# print(max_idx)
# print(min_idx)


# Find Peaks

err_allowed = 4.8/100

for i in range(100, len(price)): 
	
	"""
	### order = smooth out noice ex:order=5 more bigger less noise
	# max_idx = list(argrelextrema(price.values, np.greater, order=1)[0])
	# min_idx = list(argrelextrema(price.values, np.less, order=1)[0])

	max_idx = list(argrelextrema(price.values[:i], np.greater, order=5)[0])
	min_idx = list(argrelextrema(price.values[:i], np.less, order=5)[0])

	idx = max_idx + min_idx + [len(price.values[:i])-i]

	idx.sort()

	### v2
	# peaks = price.values[idx]
	
	current_idx = idx[-5:]
	current_pat = price.values[current_idx]
	"""
	current_idx,current_pat,start,end = peak_detect(price.values[:i])	


	### Harmonic Patterns
	XA = current_pat[1]-current_pat[0]
	AB = current_pat[2]-current_pat[1]
	BC = current_pat[3]-current_pat[2]
	CD = current_pat[4]-current_pat[3]

	moves = [XA,AB,BC,CD]

	gart = is_gartley(moves,err_allowed)
	butt = is_butterfly(moves,err_allowed)
	bat = is_bat(moves,err_allowed)
	crab = is_crab(moves,err_allowed)

	harmonics = np.array([gart,butt,bat,crab])
	labels = ['Gartely','Butterfly','Bat','Crab']

	if np.any(harmonics == 1) or np.any(harmonics == -1):
		
		for j in range(0,len(harmonics)):
			
			if harmonics[j] == 1 or harmonics[j] == -1:
				
				sense = 'Bearish' if harmonics[j] == -1 else 'Bullish'
				label = sense + labels[j] + ' Found'

				plt.title(label)
				plt.plot(np.arange(start,i+15), price.values[start:i+15])
				plt.plot(current_idx,current_pat,c='r')
				plt.show()
				

