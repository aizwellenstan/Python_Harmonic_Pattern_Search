import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

def peak_detect(price,order=5):

	max_idx = list(argrelextrema(price, np.greater, order=order)[0])
	min_idx = list(argrelextrema(price, np.less, order=order)[0])

	idx = max_idx + min_idx + [len(price)-1]

	idx.sort()
	
	current_idx = idx[-5:]

	start = min(current_idx)
	end = max(current_idx)

	current_pat = price[current_idx]

	return current_idx,current_pat,start,end

def is_gartley(moves,err_allowed):
	pattern_name = 'Gartely'	

	XA = moves[0]
	AB = moves[1]
	BC = moves[2]
	CD = moves[3]

	moves = [XA,AB,BC,CD]
	
	AB_range = np.array([0.618-err_allowed, 0.618+err_allowed])*abs(XA)
	BC_range = np.array([0.382-err_allowed, 0.886+err_allowed])*abs(AB)
	CD_range = np.array([1.27-err_allowed, 1.618+err_allowed])*abs(BC)
	
	### Bullisih
	if XA>0 and AB<0 and BC>0 and CD<0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return 1
		else:
			print('Bullish '+pattern_name+' Pattern not found')
			return np.NAN
	### Bearish
	elif XA<0 and AB>0 and BC<0 and CD>0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return -1

		else:
			print('Bearish '+pattern_name+' Pattern not found')
			return np.NAN
	
	#else:
		return np.NAN

def is_butterfly(moves,err_allowed):
	pattern_name = 'Butterfly'
	
	XA = moves[0]
	AB = moves[1]
	BC = moves[2]
	CD = moves[3]

	moves = [XA,AB,BC,CD]
	
	AB_range = np.array([0.786-err_allowed, 0.786+err_allowed])*abs(XA)
	BC_range = np.array([0.382-err_allowed, 0.886+err_allowed])*abs(AB)
	CD_range = np.array([1.618-err_allowed, 2.618+err_allowed])*abs(BC)
	
	### Bullisih
	if XA>0 and AB<0 and BC>0 and CD<0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return 1
		else:
			print('Bullish '+pattern_name+ ' Pattern not found')
			return np.NAN
	### Bearish
	elif XA<0 and AB>0 and BC<0 and CD>0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return -1

		else:
			print('Bearish '+pattern_name +' Pattern not found')
			return np.NAN
	
	else:
		return np.NAN

def is_bat(moves,err_allowed):
	pattern_name = 'Bat'
	
	XA = moves[0]
	AB = moves[1]
	BC = moves[2]
	CD = moves[3]

	moves = [XA,AB,BC,CD]
	
	AB_range = np.array([0.382-err_allowed, 0.5+err_allowed])*abs(XA)
	BC_range = np.array([0.382-err_allowed, 0.886+err_allowed])*abs(AB)
	CD_range = np.array([1.618-err_allowed, 2.618+err_allowed])*abs(BC)
	
	### Bullisih
	if XA>0 and AB<0 and BC>0 and CD<0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return 1
		else:
			print('Bullish '+pattern_name+ ' Pattern not found')
			return np.NAN
	### Bearish
	elif XA<0 and AB>0 and BC<0 and CD>0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return -1

		else:
			print('Bearish '+pattern_name +' Pattern not found')
			return np.NAN
	
	else:
		return np.NAN

def is_crab(moves,err_allowed):
	pattern_name = 'Crab'
	
	XA = moves[0]
	AB = moves[1]
	BC = moves[2]
	CD = moves[3]

	moves = [XA,AB,BC,CD]
	
	AB_range = np.array([0.382-err_allowed, 0.618+err_allowed])*abs(XA)
	BC_range = np.array([0.382-err_allowed, 0.886+err_allowed])*abs(AB)
	CD_range = np.array([2.24-err_allowed, 3.618+err_allowed])*abs(BC)
	
	### Bullisih
	if XA>0 and AB<0 and BC>0 and CD<0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return 1
		else:
			print('Bullish '+pattern_name+ ' Pattern not found')
			return np.NAN
	### Bearish
	elif XA<0 and AB>0 and BC<0 and CD>0:

		if (AB_range[0]<abs(AB)<AB_range[1] 
			and BC_range[0]<abs(BC)<BC_range[1] 
			and CD_range[0]<abs(CD)<CD_range[1]):
			
			return -1

		else:
			print('Bearish '+pattern_name +' Pattern not found')
			return np.NAN
	
	else:
		return np.NAN


