import os
from work_with_sql import *


from docx import Document

template = 'Раз.docx'

template_doc = Document('nice.docx')

count = 0
dict = {}
for table in template_doc.tables:#заменить текст в таблицах
    for row in table.rows:
        count +=1

        if row.cells[0].text == ("1"):
            continue
        if row.cells[0].text == ("Фамилия, имя, отчество (при наличии)"):
            continue
        name = row.cells[0].text #.split(" ")
        #s_o = row.cells[0].cplit(" ")[1] + row.cells[0].cplit(" ")[2]
        profession = row.cells[10].text
        if name in dict:
            if not profession in dict[name]:
                dict[name] = dict[name]+","+profession
            continue
        dict[name] = profession
        print(count)

dict1 = sorted(dict)
"""dict1 = {
    'Богомольская Валерия Арктика': "вкертолетостроение",
    "Копылова Анна Аннова": "ыовдстовотв"

}"""
a = 1
"""for d in dict1:
    a +=1
    print(str(a)+") "+ d + ":"+ dict[d])"""
os.remove("../dbs/profs.db")
create_table_profs()
for d in dict1:
    a +=1
    name = d.split(" ")[0]
    sql_insert_in_profs([d,name, dict[d]])
    print(str(a)+") "+name+" "+d + ":"+ dict[d])

#print(find_in_table_profs("Аксененкова"))