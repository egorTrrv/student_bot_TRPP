#модуль запуска. Главное меню. здесь начинаются и сюда возвращают все функции.
from classes.superBot import *
from functions.starting import *
from functions.scheduling import *


SB1 = SuperBot()
msg = SB1.input_message_from_user()
Us1 = User(msg[1])
users.update({Us1.id: Us1})
#найти юзера в бд, если найдешь, то присвоить ему номер группы
Us1.student_group = set_group(Us1.id)
while(True):
    if msg[0] == "начать":
        start(SB1, Us1)
    elif msg[0] == "расписание":
        scheduling(SB1,Us1)
    elif msg[0] == "домашние задания":
        pass
    elif msg[0] == "узнать имя преподавателя":
        pass
    elif msg[0] == "заметки":
        pass
    elif msg[0] == "изменить номер группы":
        change_number_of_group(SB1, Us1)
    else:
        SB1.launch_mm_keyboard("Введите уоманду!", Us1.id)
    msg = SB1.input_message_from_user()
