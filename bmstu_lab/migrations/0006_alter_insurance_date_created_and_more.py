# Generated by Django 4.2.5 on 2023-12-06 21:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0005_alter_insurance_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 6, 21, 0, 11, 647816, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 6, 0, 0, 11, 647779), verbose_name='Дата конца'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 7, 0, 0, 11, 647765), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmstu_lab.users', verbose_name='Пользователь'),
        ),
    ]
