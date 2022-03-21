import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="593662ffd599297e66363409dbd93f093c691c8119fa51c1c5ac4e5f58d41eaa4cad6b2e714e22c9ea72e")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

#для отправки сообщений
def send_some_message(id, message_text):
    vk_session.method("messages.send", {"user_id": id, "message": message_text+", друг.", "random_id": 0})


for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:#если это не бот сам себе отправил
            msg = event.text.lower()
            id = event.user_id
            send_some_message(id, msg)
