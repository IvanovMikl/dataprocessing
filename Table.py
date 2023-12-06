from openpyxl import load_workbook

wb = load_workbook('Results1ab.xlsx')
ws = wb.active

ws.move_range("A21:C40", rows=-20, cols=3)

wb.save('FinalResults.xlsx')