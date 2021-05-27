class Employee:

    def __init__(self, name, id_number, department, position):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__position = position

    def set_name(self, name):
        self.__name = name

    def set_id_numb(self, id_number):
        self.__id_number = id_number

    def set_depart(self, department):
        self.__department = department

    def set_pos(self, position):
        self.__position = position

    def get_name(self):
        return self.__name

    def get_id_numb(self):
        return self.__id_number

    def get_depart(self):
        return self.__department

    def get_pos(self):
        return self.__position

    def __str__(self):
        result = 'Имя: ' + self.get_name() + \
            '\nИдентификационный номер: ' + self.get_id_numb() + \
            '\nОтдел: ' + self.get_depart() + \
            '\nДолжность: ' + self.get_pos()
        return result
