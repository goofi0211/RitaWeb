# Generated by Django 2.2.2 on 2019-11-25 07:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191125_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 7, 43, 22, 853140, tzinfo=utc)),
        ),
    ]
