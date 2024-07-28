#from django.dispatch import receiver
#from django.db.models.signals import post_save
#
#from .models import Course
#
#
#@receiver(post_save, sender=Course)
#def course_update_handler(created, instance, *args, **kwargs):
#    if created:
#        return [created, instance]
#    else:
#        return instance
