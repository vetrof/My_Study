from django.shortcuts import render

# Create your views here.


def notes_page(requests):
    return render(requests, 'notes.html')
