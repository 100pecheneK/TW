"""
status:
  0 - создан, но не активен

  1 - получено задание 1 (день получения)
  2 - получено задание 1 и просрочено (на следующий день после дня получнения)
  3 - задание 1 в работе
  4 - задание 1 выполнено

  5 - получено задание 1 (день получения)
  6 - получено задание 1 и просрочено (на следующий день после дня получнения)
  7 - задание 1 в работе
  8 - задание 1 выполнено

  9 - получено задание 1 (день получения)
  10 - получено задание 1 и просрочено (на следующий день после дня получнения)
  11 - задание 1 в работе
  12 - задание 1 выполнено



current_task:
  1 - получено задание 1
  2 - получено задание 2
  3 - получено задание 3
date#_start - дата получения задания # (через 7 дней после date#_end; date1_start отсчитывается от date)
date#_end - дата выполнения задания #
"""
from django.db import models
import datetime
from datetime import timedelta


# Create your models here.
class Object(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    # При создании объекта будет создаваться зависимый от него
    def save(self, **kwargs):
        super(Object, self).save(**kwargs)
        Tw.objects.create(object=self)

    def __str__(self):
        return self.title


class Tw(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    # object_id = models.IntegerField()
    status = models.IntegerField(default=0)
    currentTask = models.IntegerField(default=1)
    # Дата создания
    date = models.CharField(max_length=100, default=datetime.date.today())
    date1_start = models.CharField(max_length=100, default=datetime.date.today() + timedelta(days=7))
    date1_end = models.CharField(max_length=100, default='')
    # date task2
    date2_start = models.CharField(max_length=100, default='')
    date2_end = models.CharField(max_length=100, default='')
    # date task3
    date3_start = models.CharField(max_length=100, default='')
    date3_end = models.CharField(max_length=100, default='')
