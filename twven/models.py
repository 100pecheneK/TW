"""
status:
  0 - создан, но не активен
  1 - получено задание (день получения)
  2 - получено задание и просрочено (на следующий день после дня получнения)
  3 - задание в работе
  4 - выполнены все 3 задания
current_task:
  0 - заданий нет (активно, когда self.status == 4)
  1 - получено задание 1
  2 - получено задание 2
  3 - получено задание 3
date#_start - дата получения задания # (через 7 дней после date#_end; date1_start отсчитывается от date)
date#_end - дата выполнения задания #
"""
from django.db import models
#
#
# class Tw(models.Model):
#     object = models.ForeignKey(Object, on_delete=models.CASCADE)
#     status = models.IntegerField(default=0)
#     currentTask = models.IntegerField(default=1)
#     # Дата создания
#     date = models.DateField(auto_now=True)
#     date1_start = models.DateField(default=None)
#     date1_end = models.DateField(default=None)
#     # date task2
#     date2_start = models.DateField(default=None)
#     date2_end = models.DateField(default=None)
#     # date task3
#     date3_start = models.DateField(default=None)
#     date3_end = models.DateField(default=None)
#
#
class Task(models.Model):
    text = models.TextField()
    taskNumber = models.IntegerField(default=0)
