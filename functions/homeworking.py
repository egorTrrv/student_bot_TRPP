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
            sub = msg[0][:36:]
            hm = find_in_table_id_and_homeworking(us.id, sub)

            if hm[0] == "":
                sb.launch_hm_keyboard(us.id, "Нет данных о ДЗ")
            else:
                sb.send_message_to_user(us.id, "ДЗ:")
                sb.launch_hm_keyboard(us.id, hm[0])
            msg = sb.input_message_from_user()
            while (True):
                print(msg)
                print(msg[0])
                if msg[0] == "вернуться в главное меню":
                    return ""
                if msg[0] == "изменить дз":
                    sb.send_message_to_user(us.id, "Введите ДЗ:")
                    msg = sb.input_message_from_user()
                    if msg[0] == "изменить дз":
                        continue
                    change_hm_in_id_and_homeworking(us.id, msg[0], sub, hm[1])
                    sb.send_message_to_user(us.id, "ДЗ изменено!")
                else:
                    sb.send_message_to_user(us.id, "Введите команду!:")
                msg = sb.input_message_from_user()
        elif msg[0] == "расписание 📜":
            return msg[0]
        elif msg[0] == "домашние задания 📚":
            return msg[0]
        elif msg[0] == "найти имя-отчество преподавателя👤":
            return msg[0]
        elif msg[0] == "заметки 📝":
            return msg[0]
        elif msg[0] == "изменить номер группы":
            return msg[0]
        else:
            sb.send_message_to_user(us.id, "Введите команду!")

        msg = sb.input_message_from_user()
