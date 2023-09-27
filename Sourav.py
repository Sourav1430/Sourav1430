import openpyxl
from openpyxl.styles import PatternFill

file = 'Book1.xlsx'
wb = openpyxl.load_workbook(file)
ws = wb.active
