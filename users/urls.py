from rest_framework.routers import SimpleRouter

from django.urls import path

from users import views
from users.apps import UsersConfig

router = SimpleRouter()
router.register('pay', views.PaymentsViewSet)

app_name = UsersConfig.name

urlpatterns = [
    path('user/create/', views.UserCreateAPI.as_view(), name='user_create'),
    path('user/', views.UserListAPI.as_view(), name='user_list'),
    path('user/<int:pk>/', views.UserRetrieveAPI.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', views.UserUpdateAPI.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDestroyAPI.as_view(), name='user_delete'),
] + router.urls
