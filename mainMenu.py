#модуль запуска. Главное меню. здесь начинаются и сюда возвращают все функции.
from classes.superBot import *
from functions.naming import *
from functions.starting import *
from functions.scheduling import *
from functions.homeworking import *
from functions.noting import *

SB1 = SuperBot()
msg = SB1.input_message_from_user()
Us1 = User(msg[1])
users.update({Us1.id: Us1})
#найти юзера в бд, если найдешь, то присвоить ему номер группы
Us1.student_group = set_group(Us1.id)
while(True):
    if msg[0] == "начать":
        start(SB1, Us1)
        msg = SB1.input_message_from_user()
        continue
    elif msg[0] == "расписание 📜":
        scheduling(SB1, Us1)
    elif msg[0] == "домашние задания 📚":
        msg[0] = homework(SB1, Us1)
        if msg[0]!="":
            continue
    elif msg[0] == "найти имя-отчество преподавателя👤":
        msg[0] = find_fio(SB1, Us1)
        if msg[0]!="":
            continue
    elif msg[0] == "заметки 📝":
        msg[0] = notes(SB1, Us1)
        if msg[0] != "":
            continue
    elif msg[0] == "изменить номер группы":
        change_number_of_group(SB1, Us1)
        msg = SB1.input_message_from_user()
        continue
    else:
        SB1.launch_mm_keyboard(Us1.id, "Введите команду!")
        msg = SB1.input_message_from_user()
        continue
    SB1.launch_mm_keyboard(Us1.id, "/главное меню")
    msg = SB1.input_message_from_user()
