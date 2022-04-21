import sqlite3
from sqlite3 import Error

name_of_database = 'number_of_groups.db'
con = sqlite3.connect(name_of_database)
sql = con.cursor()


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


def sql_insert(entities):
    ex = 'INSERT INTO number_of_groups(id, number_of_group) VALUES(?, ?)'
    sql.execute(ex, entities)
    con.commit()


def change_db(id, n_group):
    sql.execute(f"UPDATE number_of_groups SET number_of_group = '{n_group}' WHERE id = '{id}'")
    con.commit()


def find_number_of_group_in_sql(id):
    sql.execute(f"SELECT number_of_group FROM number_of_groups WHERE id = '{id}'")
    group = sql.fetchone()
    if group is None:
        return ""
    else:
        return group[0]
