# Generated by Django 4.2.2 on 2024-07-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0009_course_price_alter_lessons_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего обновления'),
        ),
    ]