from django.template import loader
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password #for hashing passwords
from .models import Users, Tasks

def homepage(request):
    return render(request, 'Homepage.html')

def login_view(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user exists
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return render(request, 'Login.html')

        #check password
        if not check_password(password, user.password):
            messages.error(request, 'Invalid username or password')
            return render(request, 'Login.html')

        #set session variables
        request.session['username'] = user.username
        request.session['role'] = user.role

        #redirect to dashboard based on role
        if user.role == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('teacher_dashboard')
        
    return render(request, 'Login.html')

def signup_view(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_admin = request.POST.get('is_admin')  # "True" or "False"
        cPassword = request.POST.get('confirm_password')

        #check if username already exists
        if Users.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'Signup.html')
        
        if Users.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please choose a different one.')
            return render(request, 'Signup.html')
        
        if cPassword != password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'Signup.html')
        
        role = 'admin' if is_admin == 'True' else 'teacher'
        
        #create new user
        Users.objects.create(username=username, email=email, password=make_password(password), role=role)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')
    
    return render(request, 'Signup.html')

def password_reset(request):
    return render(request, 'PasswordReset.html')

def admin_dashboard(request):

    #check if user is logged in using Django sessions, not sessionStorage
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'admin':
        return HttpResponseForbidden()
    
    return render(request, 'AdminDashboard.html')

def teacher_dashboard(request):
    return render(request, 'TeacherDashboard.html')

def add_task(request):

    #check if user is logged in using Django sessions, not sessionStorage
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'admin':
        return HttpResponseForbidden()
    
    #get all teachers for the dropdown
    teachers = Users.objects.filter(role='teacher')
    
    if request.method == 'POST':

        task_id = request.POST.get('taskId')
        title = request.POST.get('taskTitle')
        teacher = request.POST.get('teacherName')
        assigned_by = request.session.get('username')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        
        #check if task ID already exists
        if Tasks.objects.filter(id=task_id).exists():

            #show error
            return render(request, 'AddTask.html', {
                'teachers': teachers,
                'error': 'Task ID already exists. Please choose a unique ID.'
            })
        
        #add task to database
        Tasks.objects.create(
            id=task_id,
            title=title,
            teacher=teacher,
            assigned_by=assigned_by,
            priority=priority,
            description=description,
            status='Pending'
        )
        
        #redirect to dashboard after success
        return redirect('admin_dashboard')
    
    #if GET request just show the form
    return render(request, 'AddTask.html', {'teachers': teachers})

def edit_task(request, task_id):

    #check if user is logged in using Django sessions, not sessionStorage
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'admin':
        return HttpResponseForbidden()
    
    return render(request, 'EditTask.html')

def view_task(request, task_id):

    #check if user is logged in using Django sessions, not sessionStorage
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'admin':
        return HttpResponseForbidden()
    
    return render(request, 'ViewTask.html')

def profile(request):
    return render(request, 'Profile.html')\
    
def completed_tasks(request):
    return render(request, 'CompletedTasks.html')

def logout_view(request):

    if 'username' in request.session:
        del request.session['username']
        del request.session['role']

    return redirect('homepage')

#helper functions
def check_username(request):

    username = request.GET.get('username', '')
    exists = Users.objects.filter(username=username).exists()

    return JsonResponse({'exists': exists})

def check_email(request):

    email = request.GET.get('email', '')
    exists = Users.objects.filter(email=email).exists()

    return JsonResponse({'exists': exists})
