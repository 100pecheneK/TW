from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from objects.models import Tw
from .models import *
from django.urls import reverse
import datetime
from datetime import timedelta
from datetime import datetime as dt
from django.db.models import Q

import time

RUS = {
    0: 'объект создан и не активен для задания',
    1: 'получено задание 1',
    111: 'задание 1 просрочено',
    2: 'задание 1 в работе',
    3: 'задание 1 готово',
    4: 'получено задание 2',
    222: 'задание 2 просрочено',
    5: 'задание 2 в работе',
    6: 'задание 2 готово',
    7: 'получено задание 3',
    333: 'задание 3 просрочено',
    8: 'задание 3 в работе',
    9: 'задание 3 готово',
    10: 'получено задание 4',
    444: 'задание 4 просрочено',
    11: 'задание 4 в работе',
    12: 'задание 4 готово'
}


# Отображение всех объектов tw
def view_all(request):
    start = time.monotonic()
    # tws = Tw.objects.exclude(status=0).exclude(status=3).exclude(status=6).exclude(status=9).exclude(status=12)
    # tws_qs = Tw.objects.all()
    tws = Tw.objects.all()
    tws_status_recd = Tw.objects.filter(Q(status=1) | Q(status=4) | Q(status=7) | Q(status=10))
    tws_status_in_work = Tw.objects.filter(Q(status=2) | Q(status=5) | Q(status=8) | Q(status=11))
    tws_status_expired = Tw.objects.filter(Q(status=111) | Q(status=222) | Q(status=333) | Q(status=444))
    tws_status_done = Tw.objects.filter(Q(status=3) | Q(status=6) | Q(status=9) | Q(status=12))

    end = time.monotonic()
    timer = end - start
    context = {
        'time': timer,
        'tws': tws,
        'tws_status_recd': tws_status_recd,
        'tws_status_in_work': tws_status_in_work,
        'tws_status_expired': tws_status_expired,
        'tws_status_done': tws_status_done,

    }
    return render(request, 'tw_all.html', context)


# Отображение одного объекта tw
def detail_view(request, obj_id):
    time = (datetime.date.today()).strftime("%Y-%m-%d")
    # Объект задания
    tw = Tw.objects.get(object=obj_id)
    tw.status = RUS[tw.status]
    # Задание
    task_text = Task.objects.get(taskNumber=tw.currentTask)

    context = {
        'tw': tw,
        'time': time,
        'task_text': task_text.text,
    }
    return render(request, 'tw.html', context)


# Кнопка "Готово"
def done(request, obj_id):
    tw = Tw.objects.get(object=obj_id)
    if tw.status in (1, 2, 111):
        tw.status = 3
        tw.date1_end = datetime.date.today()
        # !Поправить разницу во времени
        tw.date2_start = (dt.strptime(str(tw.date1_end), '%Y-%m-%d') + timedelta(days=7)).strftime("%Y-%m-%d")
    elif tw.status in (4, 5, 222):
        tw.status = 6
        tw.date2_end = datetime.date.today()
        # !Поправить разницу во времени
        tw.date3_start = (dt.strptime(str(tw.date2_end), '%Y-%m-%d') + timedelta(days=7)).strftime("%Y-%m-%d")
    elif tw.status in (7, 8, 333):
        tw.status = 9
        tw.date3_end = datetime.date.today()
        # !Поправить разницу во времени
        tw.date4_start = (dt.strptime(str(tw.date3_end), '%Y-%m-%d') + timedelta(days=7)).strftime("%Y-%m-%d")
    elif tw.status in (10, 11, 444):
        tw.status = 12
        tw.date4_end = datetime.date.today()
        # !Поправить разницу во времени
        # tw.date3_start = dt.strptime(tw.date3_end, '%Y-%m-%d') + timedelta(days=7)
    tw.save()
    return HttpResponseRedirect(reverse('tw:all'))


# Кнопка "В работу"
def in_work(request, obj_id):
    tw = Tw.objects.get(object=obj_id)
    if tw.status in (1, 111):
        tw.status = 2
    elif tw.status in (4, 222):
        tw.status = 5
    elif tw.status in (7, 333):
        tw.status = 8
    elif tw.status in (10, 444):
        tw.status = 11
    tw.save()
    return HttpResponseRedirect(reverse('tw:all'))


def reload(request):
    tws = Tw.objects.all()
    for tw in tws:
        if tw.date1_start == str(datetime.date.today()):
            tw.status = 1
            tw.currentTask = 1
        elif tw.date2_start == str(datetime.date.today()):
            tw.status = 4
            tw.currentTask = 2
        elif tw.date3_start == str(datetime.date.today()):
            tw.status = 7
            tw.currentTask = 3
        elif tw.date4_start == str(datetime.date.today()):
            tw.status = 10
            tw.currentTask = 4
        elif (tw.status == 1) and (tw.date1_start < str(datetime.date.today())):
            tw.status = 111
            tw.currentTask = 1
        elif (tw.status == 4) and (tw.date2_start < str(datetime.date.today())):
            tw.status = 222
            tw.currentTask = 2
        elif (tw.status == 7) and (tw.date3_start < str(datetime.date.today())):
            tw.status = 333
            tw.currentTask = 3
        elif (tw.status == 10) and (tw.date4_start < str(datetime.date.today())):
            tw.status = 444
            tw.currentTask = 4
        tw.save()
    # return HttpResponseRedirect(reverse('tw:all'))
    return HttpResponse('OK')
