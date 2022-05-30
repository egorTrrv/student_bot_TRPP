from classes.user import *
from functions.work_with_sql import *


def start(sb, us):
    """
    Функция каманды "начать". Шлет приветсвенное сообщение и вызывает функцию изменения номера группы
    :param sb: объект класса SuperBot
    :param us: объект класса User
    :return: нет
    """
    welcome_message = "Этот бот был создан для помощи студентам МИРЭА" \
                          " Он может показывать расписание &#128220;, записывать ДЗ  &#128218;," \
                          " находить ФИО преподавателя &#128100;, делать заметки &#128221;\n" \
                          " в бета-версии расписание работает для бакалавриата институтов:\n" \
                          " &#128060; Институт информационных технологий\n" \
                          " &#129302; Институт искусственного интеллекта\n" \
                          " &#128161; Институт радиоэлектроники и информатики\n" \
                          " &#128124;Институт перспективных технологий и индустриального программирования\n" \
                          " &#128520;Институт технологий управления\n" \
                          " поиск преподаваетелей доступен для направлений подготовки " \
                          " программная инженерия, \n" \
                          " прикладная информатика\n" \
                          " информационные системы и технологии\n" \
                          " информатика и вычислительная техника\n"

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
    while ((len(answer[0])!=10)or(answer[0][4]!='-')or(answer[0][7]!='-')):
        text = "Введите настоящий номер группы! Например, ИКБО-01-20"
        sb.send_message_to_user(us.id, text)
        answer = sb.input_message_from_user()
    while find_group_in_list_of_groups(answer[0])!= True:
        text = "Введённого вами номера нет в БД! "
        sb.send_message_to_user(us.id, text)
        answer = sb.input_message_from_user()
    answer[0] = answer[0].upper()
    if us.student_group == "":
        ex = [us.id, answer[0]]
        sql_insert(ex)
    else:
        change_db(us.id, answer[0])
    us.student_group = answer[0]
    #возвращение в Глав меню
    text = "номер вашей группы сохранён:" + users[us.id].student_group
    sb.launch_mm_keyboard(us.id, text)



