from functions.work_with_sql import *

def homework(sb, us):
    text = "выберете предмет:"
    group = us.student_group
    subs = find_in_table_group_and_subs(group)
    sb.launch_kks_keyboard(us.id, subs, text)
    msg = sb.input_message_from_user()
    subs = subs.lower()
    print(msg)
    while(True):
        if msg[0][:36:] in subs:
            sb.send_message_to_user(us.id, "Вот тебе Дз чувак")
        elif msg[0] == "расписание":
            sb.send_message_to_user(us.id, "1!")
        elif msg[0] == "домашние задания":
            homework(sb, us)
        elif msg[0] == "узнать имя преподавателя":
            sb.send_message_to_user(us.id, "3!")
        elif msg[0] == "заметки":
            sb.send_message_to_user(us.id, "4!")
        elif msg[0] == "изменить номер группы":
            sb.send_message_to_user(us.id, "5!")
        else:
            sb.send_message_to_user(us.id, "Введите команду!")
        msg = sb.input_message_from_user()
