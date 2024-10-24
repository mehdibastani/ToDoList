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

/project-folder
    ├── main.py                # Main FastAPI application
    ├── kanban_board.py        # KanbanBoard class with database logic
    ├── kanban.db              # SQLite database (auto-generated)
    └── README.md              # Project documentation (this file)
    
- main.py: Contains the main FastAPI app and API routes.
- kanban_board.py: Defines the KanbanBoard class and the Task SQLModel schema.
- kanban.db: SQLite database file where tasks are stored.
- requirements.txt: All required dependencies which should be installed
- README.md: Project instructions and documentation.
