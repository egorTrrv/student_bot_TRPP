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
def find_group_in_list_of_groups(sg):
    sg = sg.upper()
    con = sqlite3.connect("C:\\Users\\Public\\bot\\functions\\list_of_groups.db")
    sql = con.cursor()
    sql.execute(f"SELECT num FROM list_of_groups WHERE student_group = '{sg}'")
    num = sql.fetchone()
    if num is not None:
        return True


def create_table_profs():
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\profs.db")
    sql = con.cursor()
    ex = 'CREATE TABLE profs(fio text PRIMARY KEY, fam text, profi text)'
    sql.execute(ex)
    con.commit()
def sql_insert_in_profs(entities):
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\profs.db")
    sql = con.cursor()
    ex = 'INSERT INTO profs(fio,fam, profi) VALUES(?,?, ?)'
    sql.execute(ex, entities)
    con.commit()

def find_in_table_profs(fam):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\profs.db")
    global sql
    sql = con.cursor()
    fio = []
    profi = []

    sql.execute(f"SELECT ALL fio FROM profs WHERE fam = '{fam}'")
    group = sql.fetchone()
    while group is not None:
        fio += [group[0]]
        group = sql.fetchone()
    sql.execute(f"SELECT ALL profi FROM profs WHERE fam = '{fam}'")
    group = sql.fetchone()
    while group is not None:
        profi += [group[0]]
        group = sql.fetchone()
    return (fio, profi)

"""-----------------------------------------------"""
def create_table_id_and_notes():
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_notes.db")
    sql = con.cursor()
    ex = 'CREATE TABLE id_and_notes(id text PRIMARY KEY, sub1 text,' \
         ' sub2 text, sub3 text, sub4 text, sub5 text, sub6 text, sub7 text,' \
         ' sub8 text, sub9 text, sub10 text, sub11 text, sub12 text, sub13 text,' \
         ' sub14 text, key_subs text)'
    sql.execute(ex)
    con.commit()

def sql_insert_in_id_and_notes(entities):
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_notes.db")
    sql = con.cursor()
    ex = 'INSERT INTO id_and_notes(id, sub1,' \
         ' sub2, sub3, sub4, sub5, sub6, sub7,' \
         ' sub8, sub9, sub10, sub11, sub12, sub13,' \
         ' sub14, key_subs) VALUES(?, ?, ?, ?, ?,' \
                              ' ?, ?, ?, ?, ?, ' \
                               '?, ?, ?, ?, ?, ' \
         '                      ?)'
    sql.execute(ex, entities)
    con.commit()


def find_in_table_id_and_notes(id, sub):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_notes.db")
    global sql
    sql = con.cursor()
    sql.execute(f"SELECT key_subs FROM id_and_notes WHERE id = '{id}'")
    sub_and_hm = sql.fetchone()
    if sub_and_hm is None:
        return ("", -2)
    if sub_and_hm == ";;":
        return ("", -1)
    sub_and_hm = sub_and_hm[0].split(";;")
    ind = -1
    for s in sub_and_hm:
        if sub == s:
            ind = sub_and_hm.index(s)+1
    if ind == -1:
        return ("", -1)
    sql.execute(f"SELECT sub{ind} FROM id_and_notes WHERE id = '{id}'")
    hm = sql.fetchone()
    if hm is None:
        return ""
    else:
        return (hm[0], ind)


def change_hm_in_id_and_notes(id, text, sub, ind):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_notes.db")
    global sql
    sql = con.cursor()
    if ind == -2:
        sql_insert_in_id_and_notes([id,"", "","","","", "","","","", "","","","", "",";;"])
        con.commit()
    if ind < 0:
        sql.execute(f"SELECT key_subs FROM id_and_notes WHERE id = '{id}'")
        sub_and_hm = sql.fetchone()
        if sub_and_hm[0] == ";;":
            sql.execute(f"UPDATE id_and_notes SET key_subs = '{sub}' WHERE id = '{id}'")
            sql.execute(f"UPDATE id_and_notes SET sub1 = '{text}' WHERE id = '{id}'")
        else:
            sub_and_hm = sub_and_hm[0] + ";;" + sub
            s_s = sub_and_hm.split(";;")
            num = s_s.index(sub)
            sql.execute(f"UPDATE id_and_notes SET key_subs = '{sub_and_hm}' WHERE id = '{id}'")
            sql.execute(f"UPDATE id_and_notes SET sub{num+1} = '{text}' WHERE id = '{id}'")
    else:
        sql.execute(f"UPDATE id_and_notes SET sub{ind} = '{text}' WHERE id = '{id}'")
    con.commit()


"""------------------------------------------------"""
def create_table_id_and_homeworking():
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_homeworking.db")
    sql = con.cursor()
    ex = 'CREATE TABLE id_and_homeworking(id text PRIMARY KEY, sub1 text,' \
         ' sub2 text, sub3 text, sub4 text, sub5 text, sub6 text, sub7 text,' \
         ' sub8 text, sub9 text, sub10 text, sub11 text, sub12 text, sub13 text,' \
         ' sub14 text, key_subs text)'
    sql.execute(ex)
    con.commit()

def sql_insert_in_id_and_homeworking(entities):
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_homeworking.db")
    sql = con.cursor()
    ex = 'INSERT INTO id_and_homeworking(id, sub1,' \
         ' sub2, sub3, sub4, sub5, sub6, sub7,' \
         ' sub8, sub9, sub10, sub11, sub12, sub13,' \
         ' sub14, key_subs) VALUES(?, ?, ?, ?, ?,' \
                              ' ?, ?, ?, ?, ?, ' \
                               '?, ?, ?, ?, ?, ' \
         '                      ?)'
    sql.execute(ex, entities)
    con.commit()


def find_in_table_id_and_homeworking(id, sub):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_homeworking.db")
    global sql
    sql = con.cursor()
    sql.execute(f"SELECT key_subs FROM id_and_homeworking WHERE id = '{id}'")
    sub_and_hm = sql.fetchone()
    if sub_and_hm is None:
        return ("", -2)
    if sub_and_hm == ";;":
        return ("", -1)
    sub_and_hm = sub_and_hm[0].split(";;")
    ind = -1
    for s in sub_and_hm:
        if sub == s:
            ind = sub_and_hm.index(s)+1
    if ind == -1:
        return ("", -1)
    sql.execute(f"SELECT sub{ind} FROM id_and_homeworking WHERE id = '{id}'")
    hm = sql.fetchone()
    if hm is None:
        return ""
    else:
        return (hm[0], ind)


def change_hm_in_id_and_homeworking(id, text, sub, ind):
    global con
    con = sqlite3.connect("C:\\Users\\Public\\bot\\dbs\\id_and_homeworking.db")
    global sql
    sql = con.cursor()
    if ind == -2:
        sql_insert_in_id_and_homeworking([id,"", "","","","", "","","","", "","","","", "",";;"])
        con.commit()
    if ind < 0:
        sql.execute(f"SELECT key_subs FROM id_and_homeworking WHERE id = '{id}'")
        sub_and_hm = sql.fetchone()
        if sub_and_hm[0] == ";;":
            sql.execute(f"UPDATE id_and_homeworking SET key_subs = '{sub}' WHERE id = '{id}'")
            sql.execute(f"UPDATE id_and_homeworking SET sub1 = '{text}' WHERE id = '{id}'")
        else:
            sub_and_hm = sub_and_hm[0] + ";;" + sub
            s_s = sub_and_hm.split(";;")
            num = s_s.index(sub)
            sql.execute(f"UPDATE id_and_homeworking SET key_subs = '{sub_and_hm}' WHERE id = '{id}'")
            sql.execute(f"UPDATE id_and_homeworking SET sub{num+1} = '{text}' WHERE id = '{id}'")
    else:
        sql.execute(f"UPDATE id_and_homeworking SET sub{ind} = '{text}' WHERE id = '{id}'")
    con.commit()



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
