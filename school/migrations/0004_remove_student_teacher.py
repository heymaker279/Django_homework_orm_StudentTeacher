# Generated by Django 4.0.5 on 2022-06-18 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_students_studentteacher_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
