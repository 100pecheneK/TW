from django.shortcuts import render
from django.http import HttpResponseRedirect
from objects.models import Tw
from django.urls import reverse
import datetime
from datetime import timedelta
from datetime import datetime as dt


# Отображение всех объектов tw
def all(request):
    tws = Tw.objects.all()
    context = {
        'tws': tws,
    }
    return render(request, 'tw_all.html', context)


# Отображение одного объекта tw
def view(request, obj_id):
    tw = Tw.objects.get(object=obj_id)
    context = {
        'tw': tw,
    }
    return render(request, 'tw.html', context)


# Кнопка "Готово"
def done(request, obj_id):
    tw = Tw.objects.get(object=obj_id)
    if tw.status in (1, 2):
        tw.status = 3
        tw.date3_end = datetime.date.today()
        # !Поправить разницу во времени
        tw.date1_start = dt.strptime(tw.date1_end, '%Y-%m-%d') + timedelta(days=7)
    elif tw.status in (4, 5):
        tw.status = 6
        tw.date2_end = datetime.date.today()
        # !Поправить разницу во времени
        tw.date2_start = dt.strptime(tw.date2_end, '%Y-%m-%d') + timedelta(days=7)
    elif tw.status in (7, 8):
        tw.status = 9
        tw.date3_end = datetime.date.today()
        # !Поправить разницу во времени
        tw.date3_start = dt.strptime(tw.date3_end, '%Y-%m-%d') + timedelta(days=7)
    tw.save()
    return HttpResponseRedirect(reverse('tw:all'))


# Кнопка "В работу"
def in_work(request, obj_id):
    tw = Tw.objects.get(object=obj_id)
    if tw.status == 1:
        tw.status = 2
    elif tw.status == 4:
        tw.status = 5
    elif tw.status == 7:
        tw.status = 8
    tw.save()
    return HttpResponseRedirect(reverse('tw:all'))

def test(request, obj_id):
    tw = Tw.objects.get(object=obj_id)
    tw.status = 1
    tw.save()
    return HttpResponseRedirect(reverse('tw:all'))

