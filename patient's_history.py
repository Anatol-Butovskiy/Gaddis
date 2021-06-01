import patient
import procedure


def main():

    procedure1 = procedure.Procedure('Врачебный осмотр ', '01.06.2021 ', 'Ирвин ', 250)
    procedure2 = procedure.Procedure('Рентгеноскопия ', '01.06.2021 ', 'Джемисон ', 500)
    procedure3 = procedure.Procedure('Анализ крови ', '01.06.2021 ', 'Смит ', 200)

    pat = patient.Patient('Иван ', 'Васильевич ', 'Круглоглазов ', 'Ул. Синеозерная, д. 3 ',
                          'Пенза ', 'Пензенская область ', '310020 ', '89047634999 ',
                          'Ирина Круглоглазова ', '89042535674 ')

    costs = procedure1.get_cost() + procedure2.get_cost() + procedure3.get_cost()

    print(pat)
    print(procedure1)
    print(procedure2)
    print(procedure3)
    print('Общая стоимость процедур: ', format(costs, '.2f'))


main()
