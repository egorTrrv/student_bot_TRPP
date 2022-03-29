"""import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="593662ffd599297e66363409dbd93f093c691c8119fa51c1c5ac4e5f58d41eaa4cad6b2e714e22c9ea72e")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


def send_some_message(id, message_text):
    '''
    базовая функция для отправки сообшения определенному пользователю
    :param id: id пользователя, которуму отправляется сообщение
    :param message_text: сообшение в формате "string"
    :return: нет
    '''
    vk_session.method("messages.send", {"user_id": id, "message": message_text+", друг.", "random_id": 0})

def start(id):
    welcome_message = "Этот бот был создан для помощи студентам МИРЭА." \
                      " Он может показывать расписание, ДЗ," \
                      " ФИО преподавателя, делать заметки"
    send_some_message(id, welcome_message)
def change_number_of_group():

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:#если это не бот сам себе отправил
            msg = event.text.lower()
            id = event.user_id
            send_some_message(id, msg)
"""