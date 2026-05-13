from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'Homepage.html')

def login_view(request):
    return render(request, 'Login.html')

def signup_view(request):
    return render(request, 'Signup.html')

def password_reset(request):
    return render(request, 'PasswordReset.html')

def admin_dashboard(request):
    return render(request, 'AdminDashboard.html')

def teacher_dashboard(request):
    return render(request, 'TeacherDashboard.html')

def add_task(request):
    return render(request, 'AddTask.html')

def edit_task(request, task_id):
    return render(request, 'EditTask.html')

def view_task(request, task_id):
    return render(request, 'ViewTask.html')

def profile(request):
    return render(request, 'Profile.html')\
    
def completed_tasks(request):
    return render(request, 'CompletedTasks.html')