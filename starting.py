from user import *


class Starting:
    def start(self, sb, us):
        welcome_message = "Этот бот был создан для помощи студентам МИРЭА." \
                          " Он может показывать расписание, ДЗ," \
                          " ФИО преподавателя, делать заметки"
        sb.send_message_to_user(us.id, welcome_message)
        self.change_number_of_group(sb, us)

    def change_number_of_group(self, sb, us):
        if us.student_group != "":
            text = "ваш текущий номер группы:" + users[us.id].student_group
            sb.send_message_to_user(us.id, text)
        text = "Введите номер вашей группы:"
        sb.send_message_to_user(us.id, text)
        answer = sb.input_message_from_user()
        us.student_group = answer[0]
        text = "номер вашей группы:" + users[us.id].student_group
        sb.send_message_to_user(us.id, text)
