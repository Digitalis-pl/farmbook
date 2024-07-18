from rest_framework import serializers

from materials.models import Course, Lessons
from materials.validators import link_validate
from payments.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[link_validate])

    class Meta:
        model = Lessons
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count_in_course = serializers.SerializerMethodField()
    lessons_in_course = serializers.SerializerMethodField()
    subscribe = serializers.SerializerMethodField()

    def get_lessons_count_in_course(self, course):
        return Lessons.objects.filter(course=course.pk).count()

    def get_lessons_in_course(self, course):
        return [lesson.name for lesson in Lessons.objects.filter(course=course.pk)]

    def get_subscribe(self, course):
        return {"subscribe": "вы подписаны на этот курс"}

    class Meta:
        model = Course
        fields = ('name', 'preview', 'description', 'lessons_count_in_course', 'lessons_in_course', 'subscribe')
