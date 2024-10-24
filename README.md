# ToDoList
This is a simple Kanban board API built with **FastAPI** and **SQLModel** for task management. It provides basic CRUD (Create, Read, Update, Delete) functionality for tasks using an SQLite database.

## Features

- Create, update, delete, and fetch tasks.
- Tasks are stored in an SQLite database using SQLModel.
- Includes API documentation with **Swagger UI**.
  
## Installation

Follow these steps to set up and run the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/mehdibastani/ToDoList.git
cd ToDoList
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
pip install virtualenv
```
#### For Unix/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```
Or manually install dependencies:
```bash
pip install fastapi[standard] sqlmodel 
```
###  4. Run the application
To start the FastAPI server, run the following command in the virtual environment:

```bash
fastapi dev main.py
```
The API will be available at http://127.0.0.1:8000.
You can interact with the API using the Swagger UI at http://127.0.0.1:8000/docs.

#### Project Structure
```
/project-folder
    ├── main.py                # Main FastAPI application
    ├── kanban_board.py        # KanbanBoard class with database logic
    ├── kanban.db              # SQLite database (auto-generated)
    └── README.md              # Project documentation (this file)
```
    
- main.py: Contains the main FastAPI app and API routes.
- kanban_board.py: Defines the KanbanBoard class and the Task SQLModel schema.
- kanban.db: SQLite database file where tasks are stored.
- requirements.txt: All required dependencies which should be installed
- README.md: Project instructions and documentation.

####  API Endpoints
#####  Get all tasks
- URL: /tasks
- Method: GET
- Response: Returns a list of all tasks.
#####  Get a task by ID
- URL: /tasks/{task_id}
- Method: GET
- Response: Returns a single task by its ID.
#####  Create a new task
- URL: /tasks
- Method: POST
- Request Body:
```
{
  "id": 1,
  "title": "New Task",
  "description": "Description of the task",
  "status": "to-do"
}
```
- Response: Returns the newly created task.

##### Update a task
- URL: /tasks/{task_id}
- Method: PUT
- Request Body:
```
{
  "title": "Updated Task Title",
  "description": "Updated description",
  "status": "in-progress"
}
```
- Response: Returns the updated task.

##### Delete a task
- URL: /tasks/{task_id}
- Method: DELETE
- Response: Returns a confirmation message after successful deletion.
