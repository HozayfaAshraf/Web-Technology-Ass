from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),          
    path('login/', views.login_view, name='login'),     
    path('signup/', views.signup_view, name='signup'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('view-task/<int:task_id>/', views.view_task, name='view_task'),
    path('profile/', views.profile, name='profile'),
    path('completed-tasks/', views.completed_tasks, name='completed_tasks'),
]