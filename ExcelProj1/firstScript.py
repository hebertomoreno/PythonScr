#openpyxl is the library for hooking up excel with python
import openpyxl, os
#Assign a workbook to a variable
wb = openpyxl.load_workbook('example.xlsx')
#Method to get the sheet names
wb.get_sheet_names()
#You can also call a specific Sheet by name
sheet = wb.get_sheet_by_name('Sheet3')
#This returns a worksheet object 
print(sheet)
#As we can see, from calling it's type
print(type(sheet))
#It has several methods, one of which
#includes the title of the sheet
print(sheet.title)

anotherSheet = wb.get_active_sheet()
print(anotherSheet)