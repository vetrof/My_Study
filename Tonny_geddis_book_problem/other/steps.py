# Упражнение по программированию 6.12

# Среднее количество шагов

# Именованные константы
JAN_DAYS = 31
FEB_DAYS = 28
MARCH_DAYS = 31
APRIL_DAYS = 30
MAY_DAYS = 31
JUNE_DAYS = 30
JULY_DAYS = 31
AUG_DAYS = 31
SEPT_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31

def main():
    step_file = open('data/steps.txt', 'r')

    avrg_step(step_file, JAN_DAYS, 'jan')
    avrg_step(step_file, FEB_DAYS, 'feb')
    avrg_step(step_file, MARCH_DAYS, 'mar')
    avrg_step(step_file, APRIL_DAYS, 'apr')
    avrg_step(step_file, MAY_DAYS, 'may')
    avrg_step(step_file, JUNE_DAYS, 'june')
    avrg_step(step_file, AUG_DAYS, 'aug')
    avrg_step(step_file, OCT_DAYS, 'oct')
    avrg_step(step_file, NOV_DAYS, 'nov')
    avrg_step(step_file, DEC_DAYS, 'dec')


def avrg_step(step_file, days, month):
    month_step = 0
    for i in range(days):
        day_step = step_file.readline()
        month_step += int(day_step)

    avrg_month = month_step / days
    print(f'avrg steep in {month} - {avrg_month:.0f} steps')

main()