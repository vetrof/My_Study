
HOUR_RATE = 2000
ONE_SQR_LITER = 0.5
ONE_SQR_MIN = 48
ONE_CAN_LITER = 5

def ink_can(sqr):
    liters = sqr * ONE_SQR_LITER
    can = liters // ONE_CAN_LITER
    if liters % ONE_CAN_LITER > 0:
        can = can + 1
    return can

def work_hour(metter_square):
    return metter_square * ONE_SQR_MIN / 60

def pay_ink(can, can_cost):
    return can * can_cost

def pay_work(sqr):
    return (sqr * ONE_SQR_MIN / 60) * HOUR_RATE

def all_pay(ink, worker):
    return ink + worker

def main():

    sqr = int(input('скока метров квадратных красить?- '))
    cost_can = int(input('сколько стоит банка 5 литров?- '))

    cans = ink_can(sqr)
    work_h = work_hour(sqr)
    cost_ink = pay_ink(cans, cost_can)
    worker_pay = pay_work(sqr)
    all_summ = all_pay(cost_ink, worker_pay)

    print(f'банок с краской поребуется {cans} штук')
    print(f'на всё про всё потребуется {work_h} часов времени')
    print(f'стоить краска будет {cost_ink} рублей')
    print(f'таджикам нужно будет заплатить {worker_pay:,.2f} руб')
    print(f'все вместе будет стоить {all_summ:,.2f} руб')

main()


