from django.views.generic import ListView
from django.shortcuts import render
from .models import StudentTeacher


def students_list(request):
    template = 'school/students_list.html'

    object_list = list(StudentTeacher.objects.all())
    student_list = []
    for student in object_list:
        students = {}
        teacher = {}
        teacher_list = []
        students['name'] = student.student.name
        students['group'] = student.student.group
        teacher['name'] = student.teacher.name
        teacher['subject'] = student.teacher.subject
        students['teacher'] = teacher_list
        if students['name'] in [i['name'] for i in student_list]:
            for stud in student_list:
                if stud['name'] == students['name']:
                    if teacher not in stud['teacher']:
                        stud['teacher'].append(teacher)
            teacher_list.append(teacher)
        if students['name'] not in [i['name'] for i in student_list]:
            teacher_list.append(teacher)
            student_list.append(students)
    context = {
        'object_list': student_list
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)