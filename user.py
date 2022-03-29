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
