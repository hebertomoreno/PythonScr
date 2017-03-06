import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
#Workbooks start off with a single sheet named
#'Sheet'
sheet = wb.get_active_sheet()

sheet.title='Spam Spam Spam'
#The spreadsheet will not be saved until you
#call the save function. 
wb.save('example_copy.xlsx')
#Whenever you edit a spreadsheet you've loaded from a
#file, you should always save the new, edited spreadsheet
#to a different filename than the original. 