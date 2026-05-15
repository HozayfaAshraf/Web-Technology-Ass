# School Task Assignment Website

![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![AJAX](https://img.shields.io/badge/AJAX-0A66C2?style=flat-square&logo=javascript&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

## Motivation & Project Overview

School task management is often split across paper, messaging apps, and manual follow-ups, which makes it hard to track assignments, deadlines, and completion status in one place. This project solves that problem with a role-based web application where administrators can create and assign tasks to teachers, and teachers can view, complete, and review their assigned work.

The application is built with Django and SQLite, and all core data is stored in the database rather than browser storage. It also uses server-side validation, role-based access control, and multiple AJAX interactions to keep the interface responsive while maintaining a clean backend-driven workflow.

## Questions and Challenges Addressed

The website was designed to answer the practical workflow challenges involved in task assignment and tracking:

* How can an admin assign tasks to specific teachers from a central dashboard?
* How can teachers view only the tasks assigned to them and update task status?
* How can task details, profile changes, and password reset flows remain fully database-driven?
* How can the system use AJAX without relying on `localStorage` for essential data?

The final implementation keeps the application simple for users while enforcing data integrity on the server.

## Architecture & Data Design

The project follows a straightforward Django architecture:

1. **Presentation Layer**: Django templates render the homepage, dashboards, task forms, and account pages.
2. **Application Layer**: `views.py` handles authentication, dashboards, CRUD logic, validation, and JSON endpoints.
3. **Data Layer**: SQLite stores users and tasks using Django models.

### Core Models

* **`Users`**: Stores username, email, password, and role (`admin` or `teacher`).
* **`Tasks`**: Stores title, assigned teacher, assigned-by admin, priority, description, status, and creation date.

### Role-Based Flow

* **Admin**: Creates tasks, views the admin dashboard, deletes tasks, edits tasks, and manages user profile information.
* **Teacher**: Views assigned tasks, opens task details, marks tasks complete, and checks completed tasks.

## Key Features

This project includes the following engineering features:

1. **Session-based authentication** using Django sessions.
2. **Password hashing** with `make_password()` and verification with `check_password()`.
3. **Role-based access control** for admin and teacher dashboards.
4. **Database-backed task management** with task assignment, editing, completion, and deletion.
5. **AJAX-driven interactions** for username checks, email checks, task lists, task completion, deletion, and task details.
6. **Server-side validation** for signup, task creation, edit task, profile update, and password reset flows.
7. **Reusable front-end behavior** using vanilla JavaScript and Django templates.
8. **Custom dashboard experience** without using the Django admin panel.

## AJAX Endpoints

The project uses AJAX in several places to keep the interface responsive:

* `GET /check-username/` - username availability check
* `GET /check-email/` - email availability check
* `GET /api/tasks/` - admin task list
* `GET /api/teacher-tasks/` - teacher task list
* `GET /api/task/<id>/` - single task details
* `POST /api/complete-task/<id>/` - mark task complete
* `POST /api/delete-task/<id>/` - delete task

## Repository Structure

```text
task_manager/
├── core/
│   ├── migrations/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── AddTask.html
│   │   ├── AdminDashboard.html
│   │   ├── CompletedTasks.html
│   │   ├── EditTask.html
│   │   ├── Homepage.html
│   │   ├── Login.html
│   │   ├── PasswordReset.html
│   │   ├── Profile.html
│   │   ├── Signup.html
│   │   ├── TeacherDashboard.html
│   │   └── ViewTask.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── task_manager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

## How to Run

### Prerequisites

* Python 3
* Django

### 1. Enter the project directory

```bash
cd task_manager
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the app at `http://127.0.0.1:8000/`.

## Team Members

- Hady Hassan El Fadaly - [Github Profile](https://github.com/hadyelfadaly)
- Hozayfa Ashraf - [Github Profile](https://github.com/HozayfaAshraf)
- Omar Waleed El Sobky - [Github Profile](https://github.com/Omarsobky)
- Yassin Mohy Eldin - [Github Profile](https://github.com/Yassin-Mohy)

## Final Notes

This project is a fully database-driven school task assignment website built with Django. It avoids `localStorage` for application state, uses server-side validation, and includes enough AJAX interactions to satisfy the Phase 3 requirements while keeping the UI responsive.

## Future Enhancements

* Add filters and search to task dashboards.
* Add task due dates and notifications.
* Add pagination for large task lists.
* Add richer analytics for admin reporting.
