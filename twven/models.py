from django.db import models


class Task(models.Model):
    text = models.TextField()
    taskNumber = models.IntegerField(default=0)
