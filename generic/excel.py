#This is intentionally created without self, if we create self then we need to create object of it to access it
#in the respective executiing script
#to avoid this self is not used here. But still this works as Global.

import openpyxl

class Excel:
    def get_data(path,sheet,row,col):
        wb = openpyxl.load_workbook((path))
        value = wb[sheet].cell(row,col).value
        print(value)
        return value