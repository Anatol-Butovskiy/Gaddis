import employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employees.dat'


def main():

    employees = load_employees()

    choice = 0

    while choice != QUIT:

        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employees)

        elif choice == ADD:
            add(employees)

        elif choice == CHANGE:
            change(employees)

        elif choice == DELETE:
            delete(employees)

    save_employees(employees)


def load_employees():
    try:
        inputfile = open(FILENAME, 'rb')
        employees_dct = pickle.load(inputfile)
        inputfile.close()
    except IOError:
        employees_dct = {}
    return employees_dct


def get_menu_choice():
    print('Меню выбора действий. ')
    print('-----------------------')
    print('1. Найти сотрудника по индентификационному номеру. ')
    print('2. Добавить сотрудника. ')
    print('3. Изменить данные сотрудника. ')
    print('4. Удалить данные сотрудника. ')
    print('5. Выйти из программы. ')
    print()

    choice = int(input('Введите выбранный пункт меню: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт меню: '))
    return choice


def look_up(employees):
    id_number = input('Введите идентификационный номер сотрудника: ')
    print(employees.get(id_number, 'Идентификационный номер не найден. '))


def add(employees):
    id_number = input('Введите идентификационный номер сотрудника: ')
    name = input('Введите имя сотрудника: ')
    department = input('Введите название отдела: ')
    position = input('Введите должность сотрудника: ')
    empl = employee.Employee(name, id_number, department, position)
    if id_number not in employees:
        employees[id_number] = empl
        print('Запись добавлена. ')
    else:
        print('Такой номер уже существует. ')


def change(employees):
    id_number = input('Введите идентификационный номер сотрудника: ')
    if id_number in employees:
        name = input('Введите имя сотрудника: ')
        department = input('Введите название отдела: ')
        position = input('Введите должность сотрудника: ')
        empl = employee.Employee(name, id_number, department, position)
        employees[id_number] = empl
        print('Информация обновлена. ')
    else:
        print('Идентификационный номер не найден. ')


def delete(employees):
    id_number = input('Введите идентификационный номер сотрудника: ')
    if id_number in employees:
        del employees[id_number]
        print('Запись удалена. ')
    else:
        print('Идентификационный номер не найден. ')


def save_employees(employees):
    outputfile = open(FILENAME, 'wb')
    pickle.dump(employees, outputfile)
    outputfile.close()


main()
