# Generated by Django 2.2.7 on 2019-11-24 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191124_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 24, 8, 57, 56, 46872, tzinfo=utc)),
        ),
    ]
