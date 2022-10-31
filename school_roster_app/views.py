# school_roster_app/views.py

from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance
my_data = {
        "school_staff": my_school.staff,
        "school_name": my_school.name 
    }


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = {
        "school_staff": my_school.staff,
        "school_name": my_school.name 
    }
        
    return render(request,"pages/staff.html", my_data)


def staff_detail(request, employee_id):
    emp = None
    for e in my_school.staff:
        if employee_id == e.employee_id:
            emp = e  
            
    my_data = {
        'staff': emp
    }
    
    return render(request, "pages/staff_detail.html",my_data)


def list_students(request):
    my_data = {
        "school_students": my_school.students,
        "school_name": my_school.name 
    }
        
    return render(request,"pages/students.html", my_data)


def student_detail(request, student_id):
    stud = None
    for s in my_school.students:
        if student_id == s.school_id:
            stud = s
            
    my_data = {
        'student': stud
    }
    
    return render(request, "pages/student_detail.html",my_data)
