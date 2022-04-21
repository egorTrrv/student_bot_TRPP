from functions.work_with_sql import *

class User:
    """
    класс для представления информации о пользвателе
    ...
    Атрибуты
    --------
    student_group : str
        группа студента
    ...
    Методы
    -------
    __init__(self, id):
        инициализация
    """
    def __init__(self, id):
        self.id = id
    student_group = ""


users = {}


def set_group(id):
    return find_number_of_group_in_sql(id)