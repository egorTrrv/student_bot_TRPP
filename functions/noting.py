from functions.work_with_sql import *

def notes(sb, us):
    text = "выберете предмет:"
    group = us.student_group
    subs = find_in_table_group_and_subs(group)
    sb.launch_kks_keyboard(us.id, subs, text)
    msg = sb.input_message_from_user()
    subs = subs.lower()

    while(True):
        if msg[0][:36:] in subs:
            sub = msg[0][:36:]
            hm = find_in_table_id_and_notes(us.id, sub)
            if hm[0] == "":
                sb.launch_notes_keyboard(us.id, "Нет данных о заметках по этому предмету")
            else:
                sb.send_message_to_user(us.id, "Заметка:")
                sb.launch_notes_keyboard(us.id, hm[0])
            msg = sb.input_message_from_user()
            while (True):
                print(msg)
                print(msg[0])
                if msg[0] == "вернуться в главное меню":
                    return ""
                if msg[0] == "изменить заметку":
                    sb.send_message_to_user(us.id, "Введите заметку:")
                    msg = sb.input_message_from_user()
                    if msg[0] == "изменить заметку":
                        continue
                    change_hm_in_id_and_notes(us.id, msg[0], sub, hm[1])
                    sb.send_message_to_user(us.id, "Заметка добавлена!")
                else:
                    sb.send_message_to_user(us.id, "Введите команду!:")
                msg = sb.input_message_from_user()
        elif msg[0] == "расписание":
            return "расписание"
        elif msg[0] == "домашние задания":
            return "домашние задания"
        elif msg[0] == "узнать имя преподавателя":
            return "узнать имя преподавателя"
        elif msg[0] == "заметки":
            return "заметки"
        elif msg[0] == "изменить номер группы":
            return "изменить номер группы"
        else:
            sb.send_message_to_user(us.id, "Введите команду!")
        """if (flag == 1):
            break"""
        msg = sb.input_message_from_user()