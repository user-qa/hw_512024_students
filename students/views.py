from django.shortcuts import render

from students.models import StudentModel


def StudentViews(request):
    students = StudentModel.objects.all()
    context = {
        'students_list': students
    }
    return render(request, 'students.html', context=context)