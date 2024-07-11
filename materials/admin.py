from django.contrib import admin

from materials.models import Course, Lessons


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)


@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'course', 'owner',)
