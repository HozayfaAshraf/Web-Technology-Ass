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
- [x] Shared JavaScript handling for reusable UI behavior
- [x] In-webpage confirmation modal for deleting tasks

#### Backend Setup (Django)
- [x] Django project initialized
- [x] SQLite database configured
- [x] URL routing configured with page routes and AJAX endpoints
- [x] View functions mapped to templates
- [x] Database models created (`Users`, `Tasks`)

#### Authentication & Security
- [x] Session-based authentication (server-side, not localStorage)
- [x] Password hashing with `make_password()`
- [x] Password verification with `check_password()`
- [x] Login view with validation
- [x] Signup view with uniqueness checks
- [x] Logout functionality
- [x] Django messages framework for error/success display
- [x] Admin-only and teacher-only access checks in views

#### API Endpoints (AJAX) - Phase 3 Requirement ✓
- [x] `GET /check-username/` - Username availability check (AJAX)
- [x] `GET /check-email/` - Email availability check (AJAX)
- [x] `GET /api/tasks/` - Admin dashboard task list
- [x] `GET /api/teacher-tasks/` - Teacher dashboard task list
- [x] `GET /api/task/<id>/` - Single task details for View Task
- [x] `POST /api/complete-task/<id>/` - Mark task complete
- [x] `POST /api/delete-task/<id>/` - Delete task from admin dashboard
- **AJAX requirement: satisfied with more than 2 scenarios** ✅

#### View Implementations
- [x] `homepage(request)` - Display homepage
- [x] `login_view(request)` - User authentication with role-based redirect
- [x] `signup_view(request)` - User registration with validation
- [x] `logout_view(request)` - Clear sessions
- [x] `add_task(request)` - Admin task creation with teacher dropdown
- [x] `check_username(request)` - AJAX endpoint
- [x] `check_email(request)` - AJAX endpoint
- [x] `admin_dashboard(request)` - Admin dashboard access control
- [x] `teacher_dashboard(request)` - Teacher dashboard access control
- [x] `view_task(request, task_id)` - Show task details to teacher
- [x] `delete_task_api(request, task_id)` - Remove task by AJAX
- [x] `complete_task_api(request, task_id)` - Mark task completed by AJAX

---

### ⚠️ STILL TO DO / PARTIAL

#### Views Still Missing or Partial

| View | Status | Priority | Effort |
|------|--------|----------|--------|
| `edit_task(request, task_id)` | Partial | HIGH | 15 min |
| `completed_tasks(request)` | Not implemented | HIGH | 10 min |
| `profile(request)` | Not implemented | MEDIUM | 15 min |
| `password_reset(request)` | Not implemented | MEDIUM | 20 min |

#### Template / UX Work Still Missing
- [ ] CompletedTasks.html - Show completed tasks from the database
- [ ] EditTask.html - Add form submission and task pre-population
- [ ] Profile.html - Add user info display and edit form
- [ ] PasswordReset.html - Add reset flow and validation
- [ ] TeacherDashboard.html - Optional search and sort over fetched tasks

#### Optional Enhancements
- [ ] Search/sort for TeacherDashboard if needed
- [ ] Better feedback messages for task updates
- [ ] Extra validation on form fields where helpful

#### Notes
- The old `localStorage` flow has been removed from the key task workflows.
- AJAX is already used in more than 2 places, so the Phase 3 AJAX requirement is satisfied.

---

## 🚀 RECOMMENDED IMPLEMENTATION ORDER (Fastest Path)

Follow this order to finish the remaining Phase 3 items efficiently:

### Step 1: Finish Remaining Views (30-45 minutes)
Implement these next:
1. `edit_task(request, task_id)` - GET/POST update task data
2. `completed_tasks(request)` - Query completed tasks from the DB
3. `profile(request)` - Show and edit user info
4. `password_reset(request)` - Add a reset form and validation

### Step 2: Template Updates (30-45 minutes)
Wire the remaining pages to database-backed data:
1. `CompletedTasks.html`
2. `EditTask.html`
3. `Profile.html`
4. `PasswordReset.html`

### Step 3: Optional Enhancements
- Add search/sort behavior to TeacherDashboard if needed
- Add better feedback messages for task updates
- Add extra validation on form fields where helpful

### Step 4: Database Check
```bash
python manage.py makemigrations
python manage.py migrate
```
Run these if you want to rebuild the SQLite schema from the models.

**Estimated remaining time: ~1 to 2 hours, depending on how much validation you want to add.**

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

---

## Notes
- Do NOT use Django Admin panel (build custom admin instead)
- Data must be in database, not localStorage
- All validation must be server-side (Django forms)
- AJAX required for at least 2 features
- Current AJAX features include signup checks, admin task listing/deletion, teacher task listing, task completion, and single-task viewing.
