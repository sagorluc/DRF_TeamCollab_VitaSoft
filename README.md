# TeamCollab Project Management Tool
## Introduction
TeamCollab is a project management tool designed to help teams collaborate efficiently. The tool includes features for managing users, projects, tasks, and comments. This README provides instructions on how to set up the project locally, migrate the database, run the server, and use the provided API endpoints.

## Featurs
* User management (registration, authentication, profile updates)
* Project management (create, update, delete, list projects)
* Task management within projects (create, update, delete, list tasks)
* Comment management on tasks (create, update, delete, list comments)

## REST API Endpoints


### Users

* Register User: POST /api/users/register/

* Login User: POST /api/users/login/

* Get User Details: GET /api/users/{id}/

* Update User: PUT/PATCH /api/users/{id}/

* Delete User: DELETE /api/users/{id}/

### Projects
* List Projects: GET /api/projects/
  
* Create Project: POST /api/projects/
  
* Retrieve Project: GET /api/projects/{id}/
  
* Update Project: PUT/PATCH /api/projects/{id}/
  
* Delete Project: DELETE /api/projects/{id}/
  
### Tasks
* List Tasks: GET /api/projects/{project_id}/tasks/
  
* Create Task: POST /api/projects/{project_id}/tasks/
  
* Retrieve Task: GET /api/tasks/{id}/
  
* Update Task: PUT/PATCH /api/tasks/{id}/
  
* Delete Task: DELETE /api/tasks/{id}/
  
### Comments
* List Comments: GET /api/tasks/{task_id}/comments/
  
* Create Comment: POST /api/tasks/{task_id}/comments/
  
* Retrieve Comment: GET /api/comments/{id}/
  
* Update Comment: PUT/PATCH /api/comments/{id}/
  
* Delete Comment: DELETE /api/comments/{id}/

## Implementation Steps
### Set up the Django Project

1. Clone the repository: <br>
   `git clone https://github.com/sagorluc/DRF_TeamCollab_VitaSoft.git
    `<br>
    `cd TeamCollab `

2. Create a virtual environment and activate it:<br>
   `python -m venv venv`<br>
   `source venv/bin/activate  # On Windows use venv\Scripts\activate`

3. Install dependencies: <br>
   `pip install -r requirements.txt`


### Design the Database Schema
1. Define the models in models.py according to the database schema plan.
2. Use Django's ORM to create relationships between models.

### Migrate the Database
1. Run migrations to create the necessary tables: <br>
   `python manage.py makemigrations`<br>
   `python manage.py migrate`

### Implement the REST API
1. Use Django REST Framework to create serializers for each model.
2. Develop views for each resource and register them with the router.
3. Implement authentication using Django REST Framework and token authentication.

### Documentation
1. Use Postman to document the API.


### Running the Server
1. Start the Django development server:<br>
   `python manage.py runserver
   `<br>


# ********** END *********