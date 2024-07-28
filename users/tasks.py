from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


@shared_task
def delete_old_user():
    '''Вариант через добавление даты обновления'''
    for user in User.objects.all():
        if user.last_login < (datetime.now() - timedelta(days=30)):
            user.is_active = False
            user.save()
