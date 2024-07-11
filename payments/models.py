from django.db import models

from materials.models import Lessons, Course
from users.models import User

# Create your models here.

null_options = {'blank': True, 'null': True}


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Клиент', **null_options)
    date = models.DateField(**null_options, verbose_name='дата оплаты')
    course = models.ManyToManyField(Course, **null_options, verbose_name='оплаченный курс')
    lesson = models.ManyToManyField(Lessons, **null_options, verbose_name='оплаченный урок')
    payments_summ = models.IntegerField(default=0, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=100, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Оплаты'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f'{self.user} - {self.payments_summ} - {self.date} - {self.course} - {self.lesson}'