import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
"""from mainMenu import MainMenu
from user import *"""
vk_session = vk_api.VkApi(token="593662ffd599297e66363409dbd93f093c691c8119fa51c1c5ac4e5f58d41eaa4cad6b2e714e22c9ea72e")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


class SuperBot():
    def send_message_to_user(self, id, message_text, keyboard=None):
        if keyboard !=None:
            vk_session.method("messages.send", {"user_id": id, "message": message_text, "random_id": 0, "keyboard": keyboard.get_keyboard()})
        else:
            vk_session.method("messages.send", {"user_id": id, "message": message_text, "random_id": 0})
    def input_message_from_user(self):
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:  # если это не бот сам себе отправил
                    msg = event.text.lower()
                    id = event.user_id
                    return [msg, id]

    class KeyboardOfMainMenu:
        vkKey = VkKeyboard(one_time=True)
        vkKey.add_button("расписание", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("домашние задания", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("узнать имя преподавателя", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("заметки", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("изменить номер группы", VkKeyboardColor.SECONDARY)

        def launch_mm_keyboard(self, sb, text, id):
            sb.send_message_to_user(id, text, self.vkKey)


"""
def send_some_message(id, message_text):
    '''
    базовая функция для отправки сообшения определенному пользователю
    :param id: id пользователя, которуму отправляется сообщение
    :param message_text: сообшение в формате "string"
    :return: нет
    '''
    vk_session.method("messages.send", {"user_id": id, "message": message_text+", друг.", "random_id": 0})
"""
'''
def start(SB, Us):
    welcome_message = "Этот бот был создан для помощи студентам МИРЭА." \
                      " Он может показывать расписание, ДЗ," \
                      " ФИО преподавателя, делать заметки"
    SB.send_message_to_user(Us.id, welcome_message)
    change_number_of_group(SB, Us)

def change_number_of_group(SB, Us):
    text = "Введите номер вашей группы:"
    SB.send_message_to_user(Us.id, text)
    answer = SB.input_message_from_user()
    Us.student_group = answer[0]
    text = "номер вашей группы:"+users[Us.id].student_group
    SB.send_message_to_user(Us.id, text)
'''
"""
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:#если это не бот сам себе отправил
            msg = event.text.lower()
            id = event.user_id
            if (msg == "начать"):
                start(id)
            else:
                #send_some_message(id, msg)
"""


"""class MainMenu():
    def start(self, sb, us):
        welcome_message = "Этот бот был создан для помощи студентам МИРЭА." \
                          " Он может показывать расписание, ДЗ," \
                          " ФИО преподавателя, делать заметки"
        sb.send_message_to_user(us.id, welcome_message)
        self.change_number_of_group(sb, us)

    def change_number_of_group(self, sb, us):
        text = "Введите номер вашей группы:"
        sb.send_message_to_user(us.id, text)
        answer = sb.input_message_from_user()
        us.student_group = answer[0]
        text = "номер вашей группы:" + users[us.id].student_group
        sb.send_message_to_user(us.id, text)"""