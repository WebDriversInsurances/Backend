# Generated by Django 4.2.8 on 2024-01-11 11:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('is_moderator', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('passport_number', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('birth_date', models.DateField(default='1999-01-01', verbose_name='Дата рождения')),
                ('address', models.CharField(default='Москва', max_length=255, verbose_name='Адрес')),
                ('phone_number', models.CharField(default='+7-999-999-99-99', max_length=17, verbose_name='Телефон')),
                ('email', models.CharField(default='asd@gmail.com', max_length=255, verbose_name='Емейл')),
                ('status', models.IntegerField(choices=[(1, 'Действует'), (2, 'Удалена')], default=1, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, default='drivers/MockImage.png', null=True, upload_to='drivers', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium_amount', models.IntegerField(default=-1, verbose_name='Банкрот')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('status', models.IntegerField(choices=[(1, 'Введён'), (2, 'В работе'), (3, 'Завершён'), (4, 'Отменён'), (5, 'Удалён')], default=1, verbose_name='Статус')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2024, 1, 11, 11, 0, 27, 367021, tzinfo=datetime.timezone.utc), verbose_name='Дата создания')),
                ('date_formation', models.DateTimeField(blank=True, null=True, verbose_name='Дата формирования')),
                ('date_complete', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
                ('drivers', models.ManyToManyField(null=True, to='insurances.driver', verbose_name='Города')),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employer', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderator', to=settings.AUTH_USER_MODEL, verbose_name='Модератор')),
            ],
            options={
                'verbose_name': 'Страховка',
                'verbose_name_plural': 'Страховки',
                'ordering': ('-date_formation',),
            },
        ),
    ]
