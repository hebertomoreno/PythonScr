#!/usr/bin/env python
import os

from PIL import Image

imgRoute = r'C:\Users\hmoreno\Documents\PythonScr\Converter\images'

os.chdir(imgRoute)

for folderName, subfolders, filenames in os.walk(imgRoute):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

	cont = 1
		
	for filename in filenames:
		print(filename)
		im = Image.open(filename)
		print(im.size)
		#im = im.rotate(270, expand=True)
		im = im.resize((816,1344),Image.ANTIALIAS)
		newName = "PODER" + str(cont) + ".png"
		im.save("png\\"+newName)
		cont+=1