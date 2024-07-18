from django.contrib import admin

from payments.models import Payments, Subscription

# Register your models here.

admin.site.register(Payments)
admin.site.register(Subscription)
