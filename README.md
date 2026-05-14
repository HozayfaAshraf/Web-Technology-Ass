# Project 3 - School Task Assignment Website

## Team Members

- Hady Hassan El Fadaly 20236113
- Hozaifa Ashraf 20236029
- Omar Waleed El Sobky 20237008
- Yassin Mohy Eldin 20236118

---

## Design & Styling

### Color Scheme:
- **Primary**: Charcoal Navy (#2c3e50) - headers, buttons
- **Accent**: Sky Blue (#3498db) - hover, highlights
- **Background**: Light Grey (#ecf0f1)
- **Text on Dark**: White (#ffffff)
- **Text on Light**: Eerie Black (#1e1e1e)

---

## Phase 3 Progress Tracker

### ✅ COMPLETED

#### Frontend (HTML/CSS/JavaScript)
- [x] All 11 HTML templates created
  - [x] Login (Hoz)
  - [x] Signup (Hoz)
  - [x] HomePage (Hoz)
  - [x] AdminDashboard (Hady)
  - [x] TeacherDashboard (Hady)
  - [x] Profile (Hady)
  - [x] AddTask (Sobky)
  - [x] CompletedTasks (Sobky)
  - [x] EditTask (Sobky)
  - [x] PasswordReset (Yassin)
  - [x] ViewTask (Yassin)
- [x] CSS styling applied
- [x] Django template tags for navigation links
- [x] Django static files configuration
- [x] Shared JavaScript file (script.js) for reusable logic

#### Backend Setup (Django)
- [x] Django project initialized
- [x] SQLite database configured
- [x] URL routing configured (15 routes + AJAX endpoints)
- [x] View functions mapped to templates
- [x] Database models created (Users, Tasks)

#### Authentication & Security
- [x] Session-based authentication (server-side, not localStorage)
- [x] Password hashing with `make_password()`
- [x] Password verification with `check_password()`
- [x] Login view with validation
- [x] Signup view with uniqueness checks
- [x] Logout functionality
- [x] Django messages framework for error/success display

#### API Endpoints (AJAX) - Phase 3 Requirement ✓
- [x] `GET /check-username/` - Username availability check (AJAX)
- [x] `GET /check-email/` - Email availability check (AJAX)
- **AJAX count: 2 scenarios completed** ✅

#### View Implementations
- [x] `homepage(request)` - Display homepage
- [x] `login_view(request)` - User authentication with role-based redirect
- [x] `signup_view(request)` - User registration with validation
- [x] `logout_view(request)` - Clear sessions
- [x] `add_task(request)` - Admin task creation with teacher dropdown
- [x] `check_username(request)` - AJAX endpoint
- [x] `check_email(request)` - AJAX endpoint

---

### ❌ TODO - CRITICAL (Phase 3 Requirements)

#### 1. Database Migrations (MUST DO FIRST)
- [ ] Run `python manage.py makemigrations`
- [ ] Run `python manage.py migrate`
- [ ] Verify Users and Tasks tables in database

#### 2. View Implementations (Follow AddTask Pattern)

| View | Status | Priority | Effort |
|------|--------|----------|--------|
| `view_task(request, task_id)` | Not implemented | HIGH | 10 min |
| `edit_task(request, task_id)` | Session check only | HIGH | 15 min |
| `completed_tasks(request)` | Not implemented | HIGH | 10 min |
| `teacher_dashboard(request)` | Session check only | HIGH | 10 min |
| `admin_dashboard(request)` | Session check only | HIGH | 10 min |
| `profile(request)` | Not implemented | MEDIUM | 15 min |
| `password_reset(request)` | Not implemented | MEDIUM | 20 min |

#### 3. Template Updates
- [ ] AdminDashboard.html - Add task/user display loop
- [ ] TeacherDashboard.html - Add assigned tasks display loop
- [ ] CompletedTasks.html - Add completed tasks display loop
- [ ] EditTask.html - Add form with task pre-population
- [ ] ViewTask.html - Add task details display
- [ ] Profile.html - Add user info display and edit form
- [ ] PasswordReset.html - Add password reset form

#### 4. Task Operations
- [ ] Task deletion functionality
- [ ] Task status updates (mark as complete)
- [ ] Task filtering and search

#### 5. Advanced Features (Optional)
- [ ] Email-based password reset
- [ ] User profile editing
- [ ] Admin system statistics

---

## 🚀 RECOMMENDED IMPLEMENTATION ORDER (Fastest Path)

Follow this order to complete Phase 3 efficiently:

### Step 1: Database Activation (5 minutes)
```bash
python manage.py makemigrations
python manage.py migrate
```
This unlocks your Users and Tasks tables. **DO THIS FIRST!**

### Step 2: View Implementations (Follow AddTask Pattern - 1 hour)
Implement views in this order:
1. `view_task(request, task_id)` - Query task, pass to template
2. `edit_task(request, task_id)` - GET: show form, POST: validate & update
3. `completed_tasks(request)` - Filter Tasks by status='Completed'
4. `admin_dashboard(request)` - Query all tasks/users
5. `teacher_dashboard(request)` - Query assigned tasks
6. `profile(request)` - Display/edit user info
7. `password_reset(request)` - Password reset form + logic

### Step 3: Template Updates (1 hour)
Add data display loops to dashboard/list templates:
- AdminDashboard.html: `{% for task in tasks %}`
- TeacherDashboard.html: `{% for task in assigned_tasks %}`
- CompletedTasks.html: `{% for task in completed_tasks %}`
- EditTask.html: Pre-populate form with task data
- ViewTask.html: Display task details

### Step 4: Task Operations (30 minutes)
- Add delete buttons/views
- Add "mark complete" functionality
- Add status update endpoints

**Total Time: ~2.5 hours to completion!**

---

## Setup & Running

### Prerequisites
```bash
# Navigate to project directory
cd task_manager

# Create virtual environment (if not done)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django
```

### Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Run Development Server
```bash
python manage.py runserver
# Visit: http://localhost:8000/
```

---

## Project Structure
```
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
│   ├── models.py ⚠️ Needs migration
│   ├── tests.py
│   ├── urls.py
│   └── views.py ⚠️ Needs implementation
├── task_manager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

---

## Notes
- Do NOT use Django Admin panel (build custom admin instead)
- Data must be in database, not localStorage
- All validation must be server-side (Django forms)
- AJAX required for at least 2 features
