from work_with_sql import *
from openpyxl import load_workbook
import os
def cr_one():
    con = sql_connection()
    sql_table(con)
    ex = [0, ""]
    sql_insert(ex)

def fill_day(num):
    wb = load_workbook('../ИИТ_2 курс_21-22_весна_11нед.xlsx')
    sheet = wb["ИИТ_2к_21-22_осень"]
    k = 0
    for j in range(6, 360 ,5):
        k+=1
        if (k%4 == 0):
            continue
        print(j)
        group = sheet.cell(row = 2, column = j).value
        F = []

        for i in range(4+12*(num-1), 16+12*(num-1)):
            if (sheet.cell(row=i, column=j).value) is None:
                F+=[""]
            else:
                str0= ""
                str1 = sheet.cell(row=i, column=j).value
                if str1 is not None:
                    str0+=str1+";;"
                else:
                    str0+=";;"
                str2 = sheet.cell(row=i, column=j+1).value
                if str2 is not None:
                    str0+=str2+";;"
                else:
                    str0 += ";;"
                str3 = sheet.cell(row=i, column=j+2).value
                if str3 is not None:
                    str0+=str3+";;"
                else:
                    str0+=";;"
                str4 = sheet.cell(row=i, column=j+3).value
                if str4 is not None:
                    str0+=str4+";;"
                else:
                    str0+=";;"
                F += [str0]
        F.insert(0,group)
        #print(F)
        sql_insert_day(F, num)
def cr_mon(num):
    #os.remove("mondays.db")
    #con = sql_connection()
    create_table_of_day(num)
    #ex = ["", "","", "","", "","", "","", "","", "",""]
    #sql_insert_mon(ex)
for i in range(1,7):
    #os.remove(f'day_{i}.db')
    cr_mon(i)
    fill_day(i)
