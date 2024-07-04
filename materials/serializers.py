from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lessons


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
