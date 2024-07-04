from rest_framework.routers import SimpleRouter

from django.urls import path

from materials.apps import MaterialsConfig
from materials import views

router = SimpleRouter()
router.register('', views.CourseViewSet)

app_name = MaterialsConfig.name

urlpatterns = [
    path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', views.LessonListAPIView.as_view(), name='lessons_List'),
    path('lesson/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/delete/', views.LessonDeleteAPIView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', views.LessonUpdateAPIView.as_view(), name='lesson_update'),

] + router.urls
