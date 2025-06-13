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

1. RestaurantApp/
    └ src/
        - └ restaurantapp/
        - └ restaurantapp/
            - └ settings.py
            - └ urls.py
            - └ asgi.py
            - └ wsgi.py
        - └ users/
            - └ models.py
            - └ serializers.py
            - └ views.py
            - └ urls.py
        - └ tasks/
            - └ models.py
            - └ serializers.py
            - └ views.py
            - └ urls.py
    - └ frontend/
        - └ angular-frontend/
    - └ manage.py
    - └ requirements.txt
    - └README.md

### Main Features

#### Authentication and User Management

* JWT Authentication.
* Creation, updating, and deletion of employees.
* Filtering according to user role.
* Private API, protected under specific authentications and permissions.

#### Task Management

* Listing, creation, updating, and deletion of tasks.
* Filtering of tasks according to the assigned employee.
* Custom actions to start or finish tasks.
* API Endpoints (example)

### API Endpoint

#### ✅ Users

* POST /api/users/login/
* POST /api/users/ (create new)
* GET /api/users/
* GET /api/users/{id}/
* PUT/PATCH/DELETE /api/users/{id}/

#### ✅ Tasks

* POST /api/tasks/
* GET /api/tasks/
* GET /api/tasks/{id}/
* PUT/PATCH/DELETE /api/tasks/{id}/
* POST /api/tasks/{id}/start/
* POST /api/tasks/{id}/stop/

### Featured Technical Implementations

✅ ModelViewSet to unify endpoints into a single view  
✅ Custom Actions (@action) in the ViewSet for task start/stop  
✅ drf_spectacular for API schema  
✅ Separation of responsibilities: tasks application and users application  
✅ Classification of responsibilities: each application has its own models, serializers, views, urls  

### Future Implementations

* Implement productivity reports.
* Implement concurrency for handling high-performance tasks.
* Implement an analytics panel for administrators.

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
