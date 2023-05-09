from django.shortcuts import render
from notepage.models import StickyNotes

# Create your views here.


def notes_page(requests):
    # todo сделать выбор цвета записки
    # todo круто если сделать фильтр по цвету.. но не обязательно
    # todo неплохо если сделать прикрепленные записки
    # todo систему авторизации и главную страницу с входом
    all_record = StickyNotes.objects.all()

    l = []
    for row in all_record:
        temp_dict = {'id': row.id,
                     'note': row.note,
                     'time': row.time,
                     'head': row.head}
        l.append(temp_dict)



    context = {'all_notes': l}

    print(context)

    return render(requests, 'notes.html', context)
