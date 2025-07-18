# RestaurantApp 🍽

## Description

RestaurantApp is a Full Stack application for the operational management of a restaurant.

This application provides a robust API to manage employees, tasks, authentications, etc., along with a frontend built in Angular that communicates through this API.
This project was conceived as a professional example intended both to complete a portfolio and to prepare for job interviews for full stack developers.

### Technology used

✅ Python/Django (Django Rest Framework) — API back-end  
✅ Postgres — relational database  
✅ JSON Web Token (SimpleJWT) — authentication  
✅ drf_spectacular — API schema generation (OpenAPI)  
✅ Angular — frontend application (SPA)  
✅ Docker (optional) — containerization  
✅ Render (optional) — cloud deployment without AWS (more economical)  

### Project Structure
```
1. RestaurantApp/
  src/Frontend
├── app/
│   ├── core/               # Application logic (services, interceptors, etc.)
│   ├── modules/            # Specific modules (each module has its own components and pages)
│   │   ├── auth/           # Authentication module
│   │   │   ├── components/ # Components inside the auth module (login form, etc.)
│   │   │   ├── pages/      # Pages inside the auth module (login, register, etc.)
│   │   │   ├── auth service  # Authentication service
│   │   │   ├── auth guard    # Authentication guard
│   │   ├── dashboard/      # Dashboard module
│   │   │   ├── components/ # Components inside the dashboard module (widgets, charts, etc.)
│   │   │   ├── pages/      # Pages inside the dashboard module (main view, etc.)
│   │   │   ├── dashboard service  # Dashboard-related service
│   ├── shared/             # Reusable components, directives, pipes
│   ├── ui/                 # Common UI components (navbar, buttons, modals, etc.)
│   │   ├── navbar/         # Navbar and other reusable UI components
│   ├── app module         # Root application module
│   ├── app-routing module # Routing configuration for the application


src/Backend
├── restaurantapp/               # Core Django project files (settings, URL config, ASGI/WSGI)
│   ├── settings.py              # Settings and configurations for the project
│   ├── urls.py                  # URL routing for the project
│   ├── asgi.py                  # ASGI configuration for asynchronous handling
│   └── wsgi.py                  # WSGI configuration for web server gateway interface
├── users/                        # User-related functionality (models, serializers, views)
│   ├── models.py                # Defines user-related models (custom user, permissions)
│   ├── serializers.py           # Serializers for user data (e.g., for API requests)
│   ├── views.py                 # Views for user-related actions (login, registration, etc.)
│   └── urls.py                  # URL routing for user-related views
├── tasks/                        # Task-related functionality (models, serializers, views)
│   ├── models.py                # Task models for managing tasks and statuses
│   ├── serializers.py           # Serializers for task data (e.g., for API requests)
│   ├── views.py                 # Views for task management and actions
│   └── urls.py                  # URL routing for task-related views
└── frontend/                     # Frontend directory for the Angular application
    └── angular-frontend/         # The actual Angular project folder
└── manage.py                     # Django's command-line tool for managing the project
└── requirements.txt              # Lists all the dependencies required for the backend
└── README.md                     # Project documentation or setup i

### Main Features

#### Authentication and User Management

- JWT Authentication.
- Creation, updating, and deletion of employees.
- Filtering according to user role.
- Private API, protected under specific authentications and permissions.

#### Task Management

- Listing, creation, updating, and deletion of tasks.
- Filtering of tasks according to the assigned employee.
- Custom actions to start or finish tasks.
- API Endpoints (example)

### API Endpoint

#### ✅ Users

- POST /api/users/login/
- POST /api/users/ (create new)
- GET /api/users/
- GET /api/users/{id}/
- PUT/PATCH/DELETE /api/users/{id}/

#### ✅ Tasks

- POST /api/tasks/
- GET /api/tasks/
- GET /api/tasks/{id}/
- PUT/PATCH/DELETE /api/tasks/{id}/
- POST /api/tasks/{id}/start/
- POST /api/tasks/{id}/stop/

### Featured Technical Implementations

✅ ModelViewSet to unify endpoints into a single view  
✅ Custom Actions (@action) in the ViewSet for task start/stop  
✅ drf_spectacular for API schema  
✅ Separation of responsibilities: tasks application and users application  
✅ Classification of responsibilities: each application has its own models, serializers, views, urls  

### Future Implementations

- Implement productivity reports.
- Implement concurrency for handling high-performance tasks.
- Implement an analytics panel for administrators.

## Installation Guide (development)

1. Clone the repository:

    > `git clone` [Link text](https://github.com/your-user/restaurantapp.git)  
    > `cd restaurantapp`

2. Load the virtual environment:

    > `python -m venv venv`
    > `source venv/bin/activate`

3. Install dependencies:

    > `pip install -r requirements.txt`

4. Perform the migrations::

    > `python manage.py migrate`

5. Start the development server:

    > `python manage.py runserver`

## Contact

If you want more information or are interested in hiring me, contact me at:
✅ LinkedIn  
✅ Portfolio  
✅ Github  

Thank you for reading! ❤️
