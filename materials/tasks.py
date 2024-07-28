from datetime import datetime, timedelta

from celery import shared_task

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from payments.models import Subscription
from users.models import User
from .models import Course

@shared_task
def send_news(course_pk, course, lesson=None):
    all_subs = Subscription.objects.filter(course=course_pk).values()
    users = User.objects.filter(pk__in=[pay['user_id'] for pay in all_subs]).values()
    email_list = [user['email'] for user in users]
    print(email_list)
    if lesson:
        send_mail(subject='Обновление курса',
                  message=f'Обновление урока {lesson} в курсе {course}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=email_list)
    else:
        send_mail(subject='Обновление курса',
                  message=f'Обновление курса {course}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=email_list)

'''вариант через сигналы'''
#@shared_task
#def remind_update(signal):
#    if signal:
#        pass
#    else:
#        send_mail(subject='Напоминание',
#                  message=f'Вы давне не обновляли курс',
#                  from_email=EMAIL_HOST_USER,
#                  recipient_list=signal.email)


@shared_task
def remind_update():
    '''Вариант через добавление даты обновления'''
    objects = Course.objects.filter(update_date__lt=datetime.now() - timedelta(hours=1)).values()
    if objects:
        users = User.objects.filter(pk__in=[obj['owner_id'] for obj in objects]).values()
        send_mail(subject='Напоминание',
                  message=f'Вы давне не обновляли курс',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user['email'] for user in users])
