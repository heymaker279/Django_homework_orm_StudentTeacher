from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Student, Teacher, StudentTeacher


class StudentTeacherInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_teacher = []
        for form in self.forms:
            if 'teacher' in form.cleaned_data.keys():
                print(form.cleaned_data['teacher'])
                if form.cleaned_data['teacher'] in list_teacher:
                    raise ValidationError('Вы уже добавили этого учителя')
                list_teacher.append(form.cleaned_data['teacher'])
                print(list_teacher)
            if len(list_teacher) == 0:
                raise ValidationError('Вы не выбрали ни одного учителя')
            return super().clean()  # вызываем базовый код переопределяемого метода


class StudentTeacherInline(admin.TabularInline):
    model = StudentTeacher
    formset = StudentTeacherInlineFormset


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [StudentTeacherInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']


# @admin.register(StudentTeacher)
# class StudentTeacherAdmin(admin.ModelAdmin):
#     # inlines = [StudentTeacherInline]
#     pass
