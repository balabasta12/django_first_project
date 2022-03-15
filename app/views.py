from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/'
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list_dir = os.listdir()
    msg = f'Список директории {list_dir}'

    return HttpResponse(msg)
    #raise NotImplemented
