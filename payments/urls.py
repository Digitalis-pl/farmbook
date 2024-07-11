from rest_framework.routers import SimpleRouter

from payments import views
from payments.apps import PaymentsConfig


router = SimpleRouter()
router.register('pay', views.PaymentsViewSet)

app_name = PaymentsConfig.name

urlpatterns = [
] + router.urls
