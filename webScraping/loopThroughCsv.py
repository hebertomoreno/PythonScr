import csv
exampleFile = open('book.csv')

exampleReader = csv.reader(exampleFile)

for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

