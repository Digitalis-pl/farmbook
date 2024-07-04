# Generated by Django 4.2.2 on 2024-07-04 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('preview', models.ImageField(upload_to='materials/materials_preview', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('preview', models.ImageField(upload_to='materials/materials_preview', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('link', models.URLField(verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
