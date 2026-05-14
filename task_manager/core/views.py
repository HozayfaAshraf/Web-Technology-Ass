from django.template import loader
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
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
    # require login and teacher role
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'teacher':
        return HttpResponseForbidden()

    return render(request, 'TeacherDashboard.html', {'username': request.session.get('username')})

def add_task(request):

    #check if user is logged in using Django sessions, not sessionStorage
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'admin':
        return HttpResponseForbidden()
    
    #get all teachers for the dropdown
    teachers = Users.objects.filter(role='teacher')
    
    if request.method == 'POST':

        title = request.POST.get('taskTitle')
        teacher = request.POST.get('teacherName')
        assigned_by = request.session.get('username')
        priority = request.POST.get('priority')
        description = request.POST.get('description')

        #resolve teacher and assigned_by to user objects
        teacher_user = Users.objects.get(username=teacher)
        assigned_by_user = Users.objects.get(username=assigned_by)

        #add task to database (use FK instances)
        Tasks.objects.create(
            title=title,
            assigned_to=teacher_user,
            assigned_by=assigned_by_user,
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
    if request.session.get('role') != 'teacher':
        return HttpResponseForbidden()
    
    task = Tasks.objects.filter(id=task_id).first()
    
    return render(request, 'ViewTask.html', {'task': task})

def profile(request):
    return render(request, 'Profile.html')\
    
def completed_tasks(request):
    # require login and teacher role
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'teacher':
        return HttpResponseForbidden()

    username = request.session.get('username')
    completed_tasks_qs = Tasks.objects.select_related('assigned_to', 'assigned_by').filter(
        assigned_to__username=username,
        status='Completed'
    )

    completed_tasks = []
    for task in completed_tasks_qs:
        completed_tasks.append({
            'id': task.id,
            'title': task.title,
            'assigned_by': task.assigned_by.username if task.assigned_by else None,
            'priority': task.priority,
            'status': task.status,
            'description': task.description,
        })

    return render(request, 'CompletedTasks.html', {'completed_tasks': completed_tasks})

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

def get_tasks_api(request):

    #return tasks with resolved usernames for frontend consumption
    tasks_qs = Tasks.objects.select_related('assigned_to', 'assigned_by').filter(assigned_by__username=request.session.get('username'))
    tasks = []
    for t in tasks_qs:
        tasks.append({
            'id': t.id,
            'title': t.title,
            'teacher': t.assigned_to.username if t.assigned_to else None,
            'priority': t.priority,
            'status': t.status,
            'description': t.description,
        })

    return JsonResponse({'tasks': tasks})

def get_teacher_tasks_api(request):

    user = request.session.get('username')

    #return tasks with resolved usernames for frontend consumption
    tasks_qs = Tasks.objects.select_related('assigned_to', 'assigned_by').filter(assigned_to__username=user)
    tasks = []
    for t in tasks_qs:
        tasks.append({
            'id': t.id,
            'title': t.title,
            'teacher': t.assigned_to.username if t.assigned_to else None,
            'assigned_by': t.assigned_by.username if t.assigned_by else None,
            'priority': t.priority,
            'status': t.status,
            'description': t.description,
        })

    return JsonResponse({'tasks': tasks})

def complete_task_api(request, task_id):
    
    if not request.session.get('username'):
        return redirect('login')
    if request.session.get('role') != 'teacher':
        return HttpResponseForbidden()

    task = get_object_or_404(Tasks, id=task_id, assigned_to__username=request.session.get('username'))
    task.status = 'Completed'
    task.save()

    return JsonResponse({'success': True})

def delete_task_api(request, task_id):
    if request.method == 'POST':
        Tasks.objects.filter(id=task_id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})