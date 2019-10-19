from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.task import periodic_task
from celery.schedules import crontab
import requests

@periodic_task(run_every=crontab(minute='*/1'), name='test')
def test():
    url = 'https://vk.com/mistermihail23'
    requests.get(url)

