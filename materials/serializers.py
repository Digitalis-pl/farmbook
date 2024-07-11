from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lessons


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    #lessons = LessonSerializer()
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count_in_course = SerializerMethodField()
    lessons_in_course = SerializerMethodField()

    def get_lessons_count_in_course(self, course):
        return Lessons.objects.filter(course=course.pk).count()

    def get_lessons_in_course(self, course):
        return [lesson.name for lesson in Lessons.objects.filter(course=course.pk)]

    class Meta:
        model = Course
        fields = ('name', 'preview', 'description', 'lessons_count_in_course', 'lessons_in_course')
