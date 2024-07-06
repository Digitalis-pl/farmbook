# Generated by Django 4.2.2 on 2024-07-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_alter_course_preview'),
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name': 'Оплаты', 'verbose_name_plural': 'Оплаты'},
        ),
        migrations.RemoveField(
            model_name='payments',
            name='course',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='lesson',
        ),
        migrations.AddField(
            model_name='payments',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, to='materials.course', verbose_name='оплаченный курс'),
        ),
        migrations.AddField(
            model_name='payments',
            name='lesson',
            field=models.ManyToManyField(blank=True, null=True, to='materials.lessons', verbose_name='оплаченный урок'),
        ),
    ]
