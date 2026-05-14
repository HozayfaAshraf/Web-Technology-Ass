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

### ⚠️ STILL TO DO / CRITICAL FOR PHASE 3

The core features are in place, but the following items **must be addressed** to meet all Phase 3 requirements. The most critical issue is removing the final instances of `localStorage` and ensuring all data flows from the database.

#### Views Still Requiring Work

| View | Status | Priority | Next Step |
|------|--------|----------|-----------|
| `edit_task(request, task_id)` | Partial | **HIGH** | Implement POST logic to save changes to the database. |
| `profile(request)` | Not Implemented | **HIGH** | Build view to fetch and display user data; create form to update it. |
| `password_reset(request)` | Not Implemented | **HIGH** | Implement server-side logic for password validation and update. |

#### Critical Template/UX Work

- [ ] **Remove `localStorage` from `EditTask.html`**: The page must fetch task data from the `edit_task` view and submit changes via a POST request.
- [ ] **Remove `localStorage` from `Profile.html`**: The page must be driven by data from the `profile` view.
- [ ] **Remove `localStorage` from `PasswordReset.html`**: The entire flow must be handled on the server.
- [ ] **Add Server-Side Validation**: Per Phase 3 requirements, add robust validation to forms in `AddTask`, `EditTask`, `Signup`, etc., to handle empty fields and invalid data.

---

## 🚀 RECOMMENDED IMPLEMENTATION ORDER (Fastest Path)

Follow this order to finish the remaining Phase 3 items efficiently:

### Step 1: Remove `localStorage` & Implement Views (45-60 minutes)
This is the highest priority.
1.  **Fix `edit_task`**:
    -   Update the `edit_task` view in `views.py` to handle GET (pre-populate form from DB) and POST (save changes to DB).
    -   Remove all `localStorage` logic from `EditTask.html`.
2.  **Implement `profile`**:
    -   Create the `profile` view to fetch the logged-in user's data.
    -   Implement a form on `Profile.html` to allow users to update their info, backed by the database.
3.  **Implement `password_reset`**:
    -   Build the server-side flow in the `password_reset` view to validate the user and update their password securely.

### Step 2: Add Server-Side Validation (15-20 minutes)
1.  Go through `add_task`, `edit_task`, and `signup_view`.
2.  Add checks to ensure required fields are not empty and handle potential errors gracefully, using the Django messages framework.

### Step 3: Final Review & Database Check
- Review all pages to ensure they work as expected.
- Run migrations if any model changes were made (unlikely).
```bash
python manage.py makemigrations
python manage.py migrate
```

**Estimated remaining time: ~1.5 to 2 hours.**

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
