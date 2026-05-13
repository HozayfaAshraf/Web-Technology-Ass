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

#### Backend Setup (Django)
- [x] Django project initialized
- [x] SQLite database configured
- [x] URL routing configured (11 routes)
- [x] View functions mapped to templates
- [x] Database models created (User, Task)

---

### ❌ TODO - CRITICAL (Phase 3 Requirements)

#### 1. Database & Models
- [ ] Create migrations for User and Task models
- [ ] Run `python manage.py makemigrations`
- [ ] Run `python manage.py migrate`
- [ ] Verify database schema

#### 2. Form Validation
- [ ] Create Django forms.py with:
  - [ ] UserForm (login, signup, profile update)
  - [ ] TaskForm (create, edit tasks)
  - [ ] PasswordResetForm
  - [ ] Field validation (required, email format, password strength, unique constraints)

#### 3. Backend Views & Business Logic
- [ ] Implement POST handlers for:
  - [ ] User login (with password verification)
  - [ ] User signup (with validation)
  - [ ] User logout
  - [ ] Password reset
  - [ ] Profile update
  - [ ] Task creation
  - [ ] Task editing
  - [ ] Task deletion
  - [ ] Task completion/status changes

#### 4. API Endpoints (AJAX Integration - REQUIRED)
**Note:** Phase 3 requires AJAX in at least 2 scenarios
- [ ] Create JSON API views:
  - [ ] `POST /api/tasks/` - Create task (AJAX)
  - [ ] `GET /api/tasks/` - Get all tasks (AJAX)
  - [ ] `GET /api/tasks/<id>/` - Get specific task (AJAX)
  - [ ] `PUT /api/tasks/<id>/` - Update task (AJAX)
  - [ ] `DELETE /api/tasks/<id>/` - Delete task (AJAX)
  - [ ] `POST /api/auth/login/` - Login (AJAX)
  - [ ] `POST /api/auth/logout/` - Logout (AJAX)
- [ ] Add `@csrf_exempt` or CSRF token handling for AJAX

#### 5. Authentication & Security
- [ ] Implement Django authentication system
- [ ] Replace sessionStorage with Django sessions (server-side)
- [ ] Add role-based access control:
  - [ ] Admin-only views
  - [ ] Teacher-only views
  - [ ] User-only views
  - [ ] Redirect unauthorized users
- [ ] Implement password hashing (Django User model)
- [ ] Add logout functionality (clear sessions)

#### 6. Frontend-Backend Integration
- [ ] Update JavaScript to use AJAX instead of localStorage:
  - [ ] Login form → AJAX to API
  - [ ] Signup form → AJAX to API
  - [ ] Task creation → AJAX to API
  - [ ] Task display → AJAX to API
  - [ ] Task editing → AJAX to API
  - [ ] Task deletion → AJAX to API
- [ ] Add loading indicators for AJAX calls
- [ ] Add error handling for failed API calls

#### 7. Custom Admin Interface
- [ ] Secure AdminDashboard.html (admin role check)
- [ ] Implement admin-only features:
  - [ ] View all users
  - [ ] View all tasks
  - [ ] Create/assign tasks
  - [ ] Delete users/tasks
  - [ ] System statistics/dashboard

#### 8. Data Persistence
- [ ] Migrate all localStorage data → Database
- [ ] Test data retrieval from database
- [ ] Verify data integrity

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
