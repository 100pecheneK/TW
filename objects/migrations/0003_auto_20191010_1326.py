# Generated by Django 2.2.6 on 2019-10-10 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0002_task_tw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tw',
            name='date',
            field=models.CharField(default=datetime.datetime(2019, 10, 10, 13, 26, 17, 12703), max_length=100),
        ),
        migrations.AlterField(
            model_name='tw',
            name='date1_end',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='tw',
            name='date1_start',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='tw',
            name='date2_end',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='tw',
            name='date2_start',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='tw',
            name='date3_end',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='tw',
            name='date3_start',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
