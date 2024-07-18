from django.urls import path

from rest_framework.routers import SimpleRouter

from payments import views
from payments.apps import PaymentsConfig


router = SimpleRouter()
router.register('pay', views.PaymentsViewSet)

app_name = PaymentsConfig.name

urlpatterns = [
    path('subscription/', views.SubscriptionController.as_view(), name='subscription_controller'),
] + router.urls
