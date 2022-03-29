#модуль запуска. Главное меню. здесь начинаются и сюда возвращают все функции.
from user import *
from superBot import SuperBot
from starting import *

SB1 = SuperBot()
msg = SB1.input_message_from_user()
Us1 = User(msg[1])
users.update({Us1.id: Us1})
while(True):
    if msg[0] == "начать":
        start(SB1, Us1)
    elif msg[0] == "расписание":
        pass
    elif msg[0] == "домашние задания":
        pass
    elif msg[0] == "узнать имя преподавателя":
        pass
    elif msg[0] == "заметки":
        pass
    elif msg[0] == "изменить номер группы":
        change_number_of_group(SB1, Us1)
    else:
        SB1.send_message_to_user(Us1.id, "Введите команду!")
    msg = SB1.input_message_from_user()
