from functions.work_with_sql import *

def find_fio(sb, us):
    text = "Введите фамилию преподавателя:"
    sb.send_message_to_user(us.id, text)
    msg = sb.input_message_from_user()
    while (True):
        if msg[0] == "расписание 📜":
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
            print(msg[0])
            print(msg[0][0])
            fam = msg[0][0].upper() + msg[0][1::]
            group = find_in_table_profs(fam)
            text = "Преподаватели, которых мы смогли найти: \n"
            for f in range(len(group[0])):
                text += f"{f+1}&#8419; "+group[0][f]
                text += ", Дисциплины: " +group[1][f]
                text += "\n\n"
            if group[0] == []:
                text += "В базе данных нет преподавателя с тайкой фамилией!"
            sb.send_message_to_user(us.id, text)
            sb.send_message_to_user(us.id, "Введите фамилию преподавателя:")
            msg = sb.input_message_from_user()

