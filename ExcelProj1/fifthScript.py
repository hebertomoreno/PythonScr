import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
#Get the sheet and store it in a variable
sheet = wb.get_sheet_by_name('Sheet1')
#print the values in a tuple
print(tuple(sheet['A1':'C3']))
#Go through the rows
for rowOfCellObjects in sheet['A1':'C3']:
	#Go through the cells in the rows
	for cellObj in rowOfCellObjects:
		#Print the coordinate and the value
		print(cellObj.coordinate, cellObj.value)
	print('--- END OF ROW ---')

print(sheet[2])
#Again, this guy from the book says that the examples should
#still work, but not really. They are actually all 
#fucking deprecated. 
#Anyway, here's the thing. The book says to use 
#sheet.columns[columnNumber], however it is deprecated
#and what we should do is sheet[columnLetter]. Apparently
#When it receives a letter, it's a column. When it receives
#a number, it's a row. Then we can cycle through the objects
#sheet.columns and sheet.rows can still be used to 
#get back all the columns or all the rows. 
for cellObj in sheet['B']:
	print(cellObj.value)