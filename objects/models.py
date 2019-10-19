from django.db import models
import datetime
from datetime import timedelta


class Object(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    # При создании объекта будет создаваться зависимый от него
    def save(self, **kwargs):
        super(Object, self).save(**kwargs)
        Tw.objects.create(object=self)

    def __str__(self):
        return self.title


# date1, date2, date3, date4 - дата получения(start)/завершения(end) задания 1, 2, 3, 4 соответсвтенно
class Tw(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    currentTask = models.IntegerField(default=1)
    date = models.CharField(max_length=100, default=datetime.date.today())
    date1_start = models.CharField(max_length=100, default=datetime.date.today() + timedelta(days=7))
    date1_end = models.CharField(max_length=100, default='')
    date2_start = models.CharField(max_length=100, default='')
    date2_end = models.CharField(max_length=100, default='')
    date3_start = models.CharField(max_length=100, default='')
    date3_end = models.CharField(max_length=100, default='')
    date4_start = models.CharField(max_length=100, default='')
    date4_end = models.CharField(max_length=100, default='')
