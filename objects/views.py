from django.shortcuts import render
from .models import *
from django.db.models import Q


# Отображение объекта и количества заданий
def view(request):
    objects = Object.objects.all()

    tws_all = Tw.objects.all().count()
    # Что бы добавить фильтр по пользователю, надо дабавить это в фильтр вначало:
    #       Q(object__title='111'),
    tws_status_recd = Tw.objects.filter(Q(status=1) | Q(status=4) | Q(status=7) | Q(status=10)).count()
    tws_status_in_work = Tw.objects.filter(Q(status=2) | Q(status=5) | Q(status=8) | Q(status=11)).count()
    tws_status_expired = Tw.objects.filter(Q(status=111) | Q(status=222) | Q(status=333) | Q(status=444)).count()
    tws_status_done = Tw.objects.filter(Q(status=3) | Q(status=6) | Q(status=9) | Q(status=12)).count()

    context = {
        'objects': objects,
        'tws_all': tws_all,
        'tws_status_recd': tws_status_recd,
        'tws_status_in_work': tws_status_in_work,
        'tws_status_expired': tws_status_expired,
        'tws_status_done': tws_status_done,
    }
    return render(request, 'index.html', context)
