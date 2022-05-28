import sqlite3
from sqlite3 import Error


global con
global sql


def sql_connection():
    try:
        global con
        return con
    except Error:
        print(Error)

def create_table_group_and_subs():
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\group_and_subs.db")
    sql = con.cursor()
    ex = 'CREATE TABLE group_and_subs(number_of_group text PRIMARY KEY, subs text)'
    sql.execute(ex)
    con.commit()

def sql_insert_in_group_and_subs(entities):
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\group_and_subs.db")
    sql = con.cursor()
    ex = 'INSERT INTO group_and_subs(number_of_group, subs) VALUES(?, ?)'
    sql.execute(ex, entities)
    con.commit()

def find_in_table_list_of_groups(num):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\list_of_groups.db")
    global sql
    sql = con.cursor()
    sql.execute(f"SELECT student_group FROM list_of_groups WHERE num = '{num}'")
    group = sql.fetchone()
    if group[0] is None:
        return ""
    else:
        return group[0]

def find_in_table_group_and_subs(group):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\group_and_subs.db")
    global sql
    sql = con.cursor()
    sql.execute(f"SELECT subs FROM group_and_subs WHERE number_of_group = '{group}'")
    group = sql.fetchone()
    if group[0] is None:
        return ""
    else:
        return group[0]

def sql_table():
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\id_and_groups.db")
    sql = con.cursor()
    ex = 'CREATE TABLE id_and_groups(id text PRIMARY KEY, number_of_group text)'
    sql.execute(ex)
    con.commit()

def sql_insert(entities):
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\id_and_groups.db")
    sql = con.cursor()
    ex = 'INSERT INTO id_and_groups(id, number_of_group) VALUES(?, ?)'
    sql.execute(ex, entities)
    con.commit()


def find_number_of_group_in_sql(id):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\id_and_groups.db")
    global sql
    sql = con.cursor()
    sql.execute(f"SELECT number_of_group FROM id_and_groups WHERE id = '{id}'")
    group = sql.fetchone()
    if group is None:
        return ""
    else:
        return group[0]

def create_list_of_groups():
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\list_of_groups.db")
    global sql
    sql = con.cursor()
    ex = 'CREATE TABLE list_of_groups(num integer PRIMARY KEY, student_group text)'
    sql.execute(ex)
    con.commit()


def insert_in_list(entities):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\list_of_groups.db")
    global sql
    sql = con.cursor()
    ex = 'INSERT INTO list_of_groups(num, student_group) VALUES(?, ?)'
    sql.execute(ex, entities)
    con.commit()

def create_table_of_day(num):
    global con
    con = sqlite3.connect(f"..\\sheds\\db\\day_{num}.db")
    global sql
    sql = con.cursor()
    ex = f'CREATE TABLE day_{num}(number_of_group text PRIMARY KEY, one text, one_d text, two text,' \
         f' two_d text, three text, three_d text, four text, four_d text, fifth text, fifth_d text, six text, six_d text)'
    sql.execute(ex)
    con.commit()



def sql_insert_day(entities, num):######
    global con
    con = sqlite3.connect(f"..\\sheds\\db\\day_{num}.db")
    global sql
    sql = con.cursor()
    ex = f'INSERT INTO day_{num}(number_of_group, one, one_d, two,' \
         ' two_d, three, three_d, four, four_d, fifth, fifth_d, six, six_d) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    sql.execute(ex, entities)
    con.commit()


def change_db(id, n_group):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\id_and_groups.db")
    global sql
    sql = con.cursor()
    sql.execute(f"UPDATE id_and_groups SET number_of_group = '{n_group}' WHERE id = '{id}'")
    con.commit()




def find_subjects_by_group(group, day):
    global con
    con = sqlite3.connect(f"C:\\Users\\Public\\bot\\sheds\\db\\day_{day}.db")
    global sql
    sql = con.cursor()
    columns = ["one", "one_d", "two", "two_d", "three", "three_d", "four", "four_d", "fifth", "fifth_d", "six", "six_d"]
    subs = []
    if (day == 7):
        return ["","","","","","","","","","","",""]
    for col in columns:
        sql.execute(f"SELECT {col} FROM day_{day} WHERE number_of_group = '{group}'")
        res = sql.fetchone()
        if res is not None:
            subs += [res[0]]
        else:
            subs +=[""]
    return subs
