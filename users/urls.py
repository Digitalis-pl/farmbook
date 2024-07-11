from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from django.urls import path

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('user/create/', views.UserCreateAPI.as_view(), name='user_create'),
    path('user/', views.UserListAPI.as_view(), name='user_list'),
    path('user/<int:pk>/', views.UserRetrieveAPI.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', views.UserUpdateAPI.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDestroyAPI.as_view(), name='user_delete'),
]
