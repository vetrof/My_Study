# Упражнение по программированию 10.6

# Расходы на лечение

# import procedure
# import patient
from objects import procedure  # классы хранятся в папке objects 
from objects import patient

def main():
    procedure_1 = procedure.Procedure('Врачебный осмотр', '8-24-2022', 'Ирвин', 250.0)
    procedure_2 = procedure.Procedure('Рентгенография', '8-24-2022', 'Джемисон', 500.0)
    procedure_3 = procedure.Procedure('Анализ крови', '8-24-2022', 'Смит', 200.0)

    pat = patient.Patient('Джеймс', 'Эдвард', 'Джоунс', '123 Мэйн стрит',
                          'Биллингс', 'Монтана', '59000', '406-555-1212',
                          'Дженни Джоунс Jones', '406-555-1213')

    print(pat)
    print(procedure_1)
    print(procedure_2)
    print(procedure_3)

# Вызвать главную функцию
if __name__ == '__main__':
    main()