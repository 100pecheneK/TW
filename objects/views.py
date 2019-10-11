from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import View
from .models import *


# Create your views here.
def view(request):
    objects = Object.objects.all()
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
        tw.save()

    context = {
        'objects': objects,
    }
    return render(request, 'index.html', context)
