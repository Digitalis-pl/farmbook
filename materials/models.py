import datetime

from django.db import models

from users.models import User

# Create your models here.

null_options = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='materials/materials_preview', verbose_name='Изображение', **null_options)
    description = models.TextField(verbose_name='Описание', **null_options)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **null_options, verbose_name='Создатель')
    price = models.IntegerField(verbose_name='Цена курса', **null_options)
    update_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата последнего обновления', **null_options)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lessons(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='materials/materials_preview', verbose_name='Изображение', **null_options)
    description = models.TextField(verbose_name='Описание', **null_options)
    link = models.URLField(verbose_name='Ссылка на видео', **null_options)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, verbose_name='Курс', **null_options)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **null_options, verbose_name='Создатель')
    price = models.IntegerField(verbose_name='Цена урока', **null_options)
    update_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата последнего обновления', **null_options)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.name} {self.link}'
