from classes.user import *


def start(sb, us):
    """
    Функция каманды "начать". Шлет приветсвенное сообщение и вызывает функцию изменения номера группы
    :param sb: объект класса SuperBot
    :param us: объект класса User
    :return: нет
    """
    welcome_message = "Этот бот был создан для помощи студентам МИРЭА." \
                          " Он может показывать расписание, ДЗ," \
                          " ФИО преподавателя, делать заметки"
    sb.send_message_to_user(us.id, welcome_message)
    change_number_of_group(sb, us)


def change_number_of_group(sb, us):
    """
    функция изменения номера группы. пересылает в главное меню с кнопками
    :param sb: объект класса SuperBot
    :param us: объект класса User
    :return: нет
    """
    if us.student_group != "":
        text = "ваш текущий номер группы:" + users[us.id].student_group
        sb.send_message_to_user(us.id, text)
    text = "Введите номер вашей группы:"
    sb.send_message_to_user(us.id, text)
    answer = sb.input_message_from_user()
    us.student_group = answer[0]
    #возвращение в Глав меню
    text = "номер вашей группы сохранён:" + users[us.id].student_group
    sb.launch_mm_keyboard(text, us.id)


