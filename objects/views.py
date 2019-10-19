from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import View
from .models import *


# Create your views here.
def view(request):
    objects = Object.objects.all()
    task_old_count = Tw.objects.filter(status=111).count()
    task_old_count += Tw.objects.filter(status=222).count()
    task_old_count += Tw.objects.filter(status=333).count()
    task_old_count += Tw.objects.filter(status=444).count()
    task_new_count = Tw.objects.filter(status=1).count()
    task_new_count += Tw.objects.filter(status=4).count()
    task_new_count += Tw.objects.filter(status=7).count()
    task_new_count += Tw.objects.filter(status=10).count()
    task_in_work_count = Tw.objects.filter(status=2).count()
    task_in_work_count += Tw.objects.filter(status=5).count()
    task_in_work_count += Tw.objects.filter(status=8).count()
    task_in_work_count += Tw.objects.filter(status=11).count()
    task_all = Tw.objects.all().count()
    context = {
        'objects': objects,
        'task_old_count': task_old_count,
        'task_new_count': task_new_count,
        'task_in_work_count': task_in_work_count,
        'task_all': task_all,
    }
    return render(request, 'index.html', context)
