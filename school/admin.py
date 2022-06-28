from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Student, Teacher, StudentTeacher


class StudentTeacherInlineFormset(BaseInlineFormSet):
    def clean(self):
        print(set([form.cleaned_data.get('teacher') for form in self.forms if form.cleaned_data.get('teacher') != None]))
        if len(set([form.cleaned_data.get('teacher') for form in self.forms if
                    form.cleaned_data.get('teacher') != None])) != len(
                [form.cleaned_data.get('teacher') for form in self.forms if form.cleaned_data.get('teacher') != None]):
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
