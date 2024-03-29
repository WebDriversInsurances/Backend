# Generated by Django 4.2.8 on 2023-12-19 17:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('admin', models.BooleanField(default=False, verbose_name='Админ')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterField(
            model_name='insurance',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 17, 27, 37, 386398, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 18, 20, 27, 37, 386366), verbose_name='Дата конца'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 19, 20, 27, 37, 386353), verbose_name='Дата начала'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bmstu_lab.users', verbose_name='Пользователь'),
        ),
    ]
