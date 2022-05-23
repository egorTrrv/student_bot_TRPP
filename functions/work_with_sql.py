import sqlite3
from sqlite3 import Error

name_of_database1 = 'number_of_groups.db'
name_of_database_1= 'day_1.db'
name_of_database_2= 'day_2.db'
name_of_database_3= 'day_3.db'
name_of_database_4= 'day_4.db'
name_of_database_5= 'day_5.db'
name_of_database_6= 'day_6.db'
global con
global sql


def sql_connection():
    try:
        global con
        return con
    except Error:
        print(Error)


def sql_table(con):
    ex = 'CREATE TABLE number_of_groups(id text PRIMARY KEY, number_of_group text)'
    global sql
    sql.execute(ex)
    con.commit()

def create_table_of_day(num):
    global con
    con = sqlite3.connect(f"day_{num}.db")
    global sql
    sql = con.cursor()
    ex = f'CREATE TABLE day_{num}(number_of_group text PRIMARY KEY, one text, one_d text, two text,' \
         f' two_d text, three text, three_d text, four text, four_d text, fifth text, fifth_d text, six text, six_d text)'
    sql.execute(ex)
    con.commit()

def sql_insert(entities):
    ex = 'INSERT INTO number_of_groups(id, number_of_group) VALUES(?, ?)'
    sql.execute(ex, entities)
    con.commit()

def sql_insert_day(entities, num):######
    ex = f'INSERT INTO day_{num}(number_of_group, one, one_d, two,' \
         ' two_d, three, three_d, four, four_d, fifth, fifth_d, six, six_d) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    sql.execute(ex, entities)
    con.commit()


def change_db(id, n_group):
    sql.execute(f"UPDATE number_of_groups SET number_of_group = '{n_group}' WHERE id = '{id}'")
    con.commit()


def find_number_of_group_in_sql(id):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\number_of_groups.db")
    global sql
    sql = con.cursor()
    sql.execute(f"SELECT number_of_group FROM number_of_groups WHERE id = '{id}'")
    group = sql.fetchone()
    if group is None:
        return ""
    else:
        return group[0]


def find_subjects_by_group(group, day):
    global con
    con = sqlite3.connect(f"C:\\Users\\Public\\bot\\functions\\day_{day}.db")
    global sql
    sql = con.cursor()
    columns = ["one", "one_d", "two", "two_d", "three", "three_d", "four", "four_d", "fifth", "fifth_d", "six", "six_d"]
    subs = []
    for col in columns:
        sql.execute(f"SELECT {col} FROM day_{day} WHERE number_of_group = '{group}'")
        subs += [sql.fetchone()[0]]
    return subs
