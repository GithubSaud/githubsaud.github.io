# Generated by Django 4.0.6 on 2022-08-19 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 23, 23, 14, 855427), verbose_name='date published'),
        ),
    ]
