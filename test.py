import openpyxl

wb = openpyxl.load_workbook('Output.xlsx')
ws = wb['Sheet1']
# This will fail if there is no hyperlink to target
print(ws.cell(row=2, column=12).hyperlink.target)
