# Generated by Django 4.2.5 on 2023-11-21 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 21, 21, 1, 2, 696140, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]
