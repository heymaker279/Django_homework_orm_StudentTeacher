from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    teacher = models.ManyToManyField(Teacher, through='StudentTeacher')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class StudentTeacher(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учетеля'