import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType #связь с ботом
from vk_api.keyboard import VkKeyboard, VkKeyboardColor #клавиатура(кнопки)

#связь с ботом
vk_session = vk_api.VkApi(token="593662ffd599297e66363409dbd93f093c691c8119fa51c1c5ac4e5f58d41eaa4cad6b2e714e22c9ea72e")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


class SuperBot():
    """
    Класс, представляющий бота. Для отправки и принятия сообшений, настройки клавиатуры
    ...
    Методы
    -------
    send_message_to_user(self, id, message_text, keyboard=None):
        отправляет сообщение пользователю
    input_message_from_user(self):
        принимает сообшение от пользователя
    ...
    Классы
    _____
    KeyboardOfMainMenu
        настройка кнопок главного меню
    чтобы у пользователя появилилсь кнопки, нужно отправить ему какоето-то
     сообщение в функции launch_mm_keyboard
    """
    def send_message_to_user(self, id, message_text, keyboard=None):
        """
        отправить сообщение пользователю
        :param id: id пользователя, (int)
        :param message_text: текст сообщения, (string)
        :param keyboard: параметры клавиатуры, не обязательно(объект VkKeyboard)
        :return: нет
        """
        if keyboard is not None:
            vk_session.method("messages.send", {"user_id": id, "message": message_text, "random_id": 0,
                                                "keyboard": keyboard.get_keyboard()})
        else:
            vk_session.method("messages.send", {"user_id": id, "message": message_text, "random_id": 0})

    def input_message_from_user(self):
        """
        получить сообшение от пользвателя.
        :return: [msg, id], список, где msg - текст сообщения, id - пользовательский id
        """
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:  # если это не бот сам себе отправил
                    msg = event.text.lower()
                    id = event.user_id
                    return [msg, id]

    class KeyboardOfMainMenu:
        """
        Класс для настройки главного меню.
        ...

        Атрибуты:
        ---------
            vkKey: объект класса VkKeyboard()
            хранит свойства клавиатуры

        """
        vkKey = VkKeyboard(one_time=True, inline=False)#one_time=True чтобы клавиатура исчезла после нажатия
        vkKey.add_button("расписание", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("домашние задания", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("узнать имя преподавателя", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("заметки", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("изменить номер группы", VkKeyboardColor.SECONDARY)

    class KeyboardOfSchedule:
        vkKey = VkKeyboard(one_time=True)#one_time=True чтобы клавиатура исчезла после нажатия
        vkKey.add_button("на сегодня", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("на завтра", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("на текущую неделю", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("на следующую неделю", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("вернуться в главное меню", VkKeyboardColor.SECONDARY)

    mm_keyboard = KeyboardOfMainMenu().vkKey
    schedule_keyboard = KeyboardOfSchedule().vkKey
    def launch_mm_keyboard(self, text, id):
        """
        функция отправки сообщения и установки клавиатуры

        :param text: текст сообщения (string)
        :param id: id пользователя (int)
        :return: нет
        """
        self.send_message_to_user(id, text, self.mm_keyboard)
    def launch_schedule_keyboard(self, text, id):
        """
        функция отправки сообщения и установки клавиатуры

        :param text: текст сообщения (string)
        :param id: id пользователя (int)
        :return: нет
        """
        self.send_message_to_user(id, text, self.schedule_keyboard)
