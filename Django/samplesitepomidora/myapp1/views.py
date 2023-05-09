from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.


def index_page(request):

    # обновляем данные в таблице
    x = Worker.objects.get(id=3)
    x.salary = 100000
    x.save()

    # добавляем новую запись в таблицу
    # new_worker = Worker(name='baboon', second_name='banana', salary=60000)
    # new_worker.save()

    # получаем все строки из таблицы
    all_worker = Worker.objects.all()
    print(all_worker)

    # получаем данные через фильтр
    worker_filter = Worker.objects.filter(salary=25)
    print(worker_filter)

    # пробегаемся по всем данным циклом
    for person in all_worker:
        print(person.name, person.second_name, person.salary)

    return render(request, 'index.html')

