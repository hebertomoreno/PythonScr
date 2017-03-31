'''The time module

	The built-in time module allows our Python programs to read the system clock for the
	current time. 
'''

import time
'''time.time() returns the amount of seconds
since the Unix Epoch. The unix epoch is 12 am, January 1st 1970.'''
time.time()

'''Epoch timestamps can be used to profile code, that is, measure how long
a piece of code takes to run. '''

def calcProd():
	#Calculate the product of the first 100,000 numbers.
	product = 1
	for i in range(1,100000):
		product = product * i
	return product

startTime = time.time()

prod = calcProd()

endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))) )

print('Took %s seconds to calculate.' % (endTime - startTime))
'''The round function rounds the number to the number of 
decimals indicates by the second parameter'''
print(round(endTime-startTime, 2))