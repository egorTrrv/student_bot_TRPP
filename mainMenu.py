"""import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType"""
from user import *
from superBot import SuperBot
from starting import Starting
"""vk_session = vk_api.VkApi(token="593662ffd599297e66363409dbd93f093c691c8119fa51c1c5ac4e5f58d41eaa4cad6b2e714e22c9ea72e")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)"""


SB1 = SuperBot()
msg = SB1.input_message_from_user()
Us1 = User(msg[1])
users.update({Us1.id: Us1})
while(True):
    if msg[0] == "начать":
        st = Starting()
        st.start(SB1, Us1)
    elif msg[0] == "расписание":
        pass
    elif msg[0] == "домашние задания":
        pass
    elif msg[0] == "узнать имя преподавателя":
        pass
    elif msg[0] == "заметки":
        pass
    elif msg[0] == "изменить номер группы":
        st = Starting()
        st.change_number_of_group(SB1, Us1)
    else:
        SB1.send_message_to_user(Us1.id, "Введите команду!")
    msg = SB1.input_message_from_user()
