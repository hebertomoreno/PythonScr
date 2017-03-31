import time

print('Tap your rhythm. ')
input()
print('Started.')

startTime = time.time()
lastTime = startTime

try:
	while True:
		input()
		beat = time.time() - lastTime
		bpm = round(60/beat)

		print('BPM = %s' % (bpm), end='')

		lastTime = time.time() #reset the last lap time

except KeyboardInterrupt:
	#Handle the Ctrl-C exception to keep its error message from displaying
	print('\nDone.')