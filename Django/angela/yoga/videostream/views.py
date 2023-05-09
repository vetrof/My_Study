from django.http import StreamingHttpResponse
from django.shortcuts import render
from access.views import access_check

from users.models import User
from videostream.services import open_file
from lessons.models import Pay_lessons, Lessons


def get_streaming_video(request, pk: int):

    access = access_check(request, pk)

    if access:

        file, status_code, content_length, content_range = open_file(request, pk)
        response = StreamingHttpResponse(file, status=status_code,
                                         content_type='video/mp4')

        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(content_length)
        response['Cache-Control'] = 'no-cache'
        response['Content-Range'] = content_range
        return response

    else:
        return render(request, 'lessons/index.html')

