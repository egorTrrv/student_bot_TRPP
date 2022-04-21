def scheduling(sb, us):
    text = "введите команду:"
    sb.launch_schedule_keyboard(text, us.id)
    msg = sb.input_message_from_user()
    while(True):
        if msg[0] == "на сегодня":
            sb.send_message_to_user(us.id, "1!")
        elif msg[0] == "на завтра":
            sb.send_message_to_user(us.id, "2!")
        elif msg[0] == "на текущую неделю":
            sb.send_message_to_user(us.id, "3!")
        elif msg[0] == "на следующую неделю":
            sb.send_message_to_user(us.id, "4!")
        elif msg[0] == "вернуться в главное меню":
            text = "вернуться в главное меню*"
            sb.launch_mm_keyboard(text, us.id)
        else:
            sb.send_message_to_user(us.id, "Введите команду!")
        msg = sb.input_message_from_user()
