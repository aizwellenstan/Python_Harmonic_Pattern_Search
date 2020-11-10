import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

# Import historical data

data = pd.read_csv('Data/JP225.csv')

#data.columns = [['LocalTime', 'open', 'high', 'low', 'close', 'vol']]
data.columns = [c.strip().lower().replace(' ','_') for c in data.columns]

data = data.drop_duplicates(keep=False)

#data.Date = pd.to_datetime(data.Date, format='%d.%m.%Y %H:%M:%S.%f')

data = data.set_index(data.local_time)

data = data[['open','high','low','close','volume']]


price = data.close.iloc[:100]


# Fubd our relative extrema

max_idx = argrelextrema(price.values, np.greater, order=1)
min_idx = argrelextrema(price.values, np.less, order=1)

print(max_idx)
print(min_idx)
