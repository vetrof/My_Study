# access check
from lessons.models import Pay_lessons, Lessons


def access_check(request, pk):
    access = False
    curent_user = request.user.username
    current_user_id = request.user.id
    current_video_id = pk
    current_pays = []
    pays = Pay_lessons.objects.filter(user=current_user_id)
    its_free = Lessons.objects.filter(id=current_video_id, free=True)

    for i in pays:
        current_pays.append(i.lesson.id)

    if curent_user:
        if current_video_id in current_pays or its_free:
            access = True

    return access
