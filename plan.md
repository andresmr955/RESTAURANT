# 🧠 Project Plan: Task Management System for a Restaurant

## 🎯 General Objective

Create a web application to manage employees in a restaurant, record work time and assign tasks by an administrator.General Objective.

---

## 👥 User Roles

### 👤 Administrator

- Create employee accounts.
- Assign tasks to employees.
- View history of completed tasks.
- Measure productivity based on time.

### 👨‍🍳 Employee

- Log in.
- View assigned tasks.
- Mark tasks as completed.
- Record start and end time per task.

---

## ✅ MVP (Minimum Viable Product) Functionalities

- [ ] Secure registration and login.
- [ ] Different control panel for admin and employee.
- [ ] Assignment and visualization of tasks.
- [ ] Worked time registration.
- [ ] Productivity report.

---

## 🛠️ Technologies

| Area          | Tool          |
|---------------|----------------------|
| Backend       | Python (Flask)       |
| Frontend      | HTML, CSS, Bootstrap, Angular |
| Database      | SQLite (Then PostgreSQL) |
| Login         | Django-Login          |
| Security      | Django Hashers Security    |
| Deployment    | (Future) Render o Heroku |

---

## 🗂️ Project Structure

/app
/static # files CSS, JS
/templates # files HTML
init.py # Initialization of Django
models.py # Models de SQLAlchemy
urls.py # Server routes
forms.py # Forms WTForms (optional)
config.py # General configuration
requirements.txt # Dependencies

---

## 🧮 Database Design (Initial Model)

### 🧑 User

- id (int, PK)
- name (string)
- email (string, unique)
- password (hashed)
- rol (string: 'admin' o 'employee')

### 📋 Task

- id (int, PK)
- title (string)
- description (text)
- assigned_to (FK a user)
- assigned (string: pending, in progress, completed)
- time_start (datetime)
- time_end (datetime)

---

## 📅 Next steps
