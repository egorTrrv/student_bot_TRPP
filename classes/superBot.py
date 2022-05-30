from vk_api.longpoll import VkLongPoll, VkEventType #связь с ботом

#связь с ботом
from classes.homework_keyboard import *

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
        vkKey = VkKeyboard(one_time=False, inline=False)#one_time=True чтобы клавиатура исчезла после нажатия
        vkKey.add_button("расписание &#128220;", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("домашние задания &#128218;", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("найти имя-отчество преподавателя&#128100;", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("заметки &#128221;", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("изменить номер группы", VkKeyboardColor.SECONDARY)

    class KeyboardOfHomework:
        vkKey = VkKeyboard(one_time=False)  # one_time=True чтобы клавиатура исчезла после нажатия
        vkKey.add_button("изменить ДЗ", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("вернуться в главное меню", VkKeyboardColor.SECONDARY)
    class KeyboardOfNotes:
        vkKey = VkKeyboard(one_time=False)#one_time=True чтобы клавиатура исчезла после нажатия
        vkKey.add_button("изменить заметку", VkKeyboardColor.SECONDARY)
        vkKey.add_line()
        vkKey.add_button("вернуться в главное меню", VkKeyboardColor.SECONDARY)
    class KeyboardOfSchedule:
        vkKey = VkKeyboard(one_time=False)#one_time=True чтобы клавиатура исчезла после нажатия
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
    hm_keyboard = KeyboardOfHomework().vkKey
    notes_keyboard = KeyboardOfNotes().vkKey

    schedule_keyboard = KeyboardOfSchedule().vkKey

    def launch_notes_keyboard(self, id, text):
        """
        функция отправки сообщения и установки клавиатуры

        :param text: текст сообщения (string)
        :param id: id пользователя (int)
        :return: нет
        """
        self.send_message_to_user(id, text, self.notes_keyboard)

    def launch_hm_keyboard(self, id, text):
        """
        функция отправки сообщения и установки клавиатуры

        :param text: текст сообщения (string)
        :param id: id пользователя (int)
        :return: нет
        """
        self.send_message_to_user(id, text, self.hm_keyboard)
    def launch_mm_keyboard(self, id, text):
        """
        функция отправки сообщения и установки клавиатуры

        :param text: текст сообщения (string)
        :param id: id пользователя (int)
        :return: нет
        """
        self.send_message_to_user(id, text, self.mm_keyboard)
    def launch_schedule_keyboard(self,id, text):
        """
        функция отправки сообщения и установки клавиатуры

        :param text: текст сообщения (string)
        :param id: id пользователя (int)
        :return: нет
        """
        self.send_message_to_user(id, text, self.schedule_keyboard)


    def launch_kks_keyboard(self, id, subs, text):
        #kks = KeyboardOfSubjects().vkKey
        #kks1 = KeyboardOfSubjects().vkKey1
        keyboards = create_keybpoards(subs)
        print(keyboards[0])
        self.send_message_to_user(id, text, keyboards[0])
        if len(keyboards) > 1:
            for k in range(1, len(keyboards)):
                self.send_message_to_user(id, "&#8597;", keyboards[k])

