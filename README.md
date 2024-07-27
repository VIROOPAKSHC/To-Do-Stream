# To-Do-Stream App

This is a simple To-Do List web application built with Streamlit and SQLite. It allows users to add, update, delete, and view tasks with priorities and dates. The tasks are stored in a local SQLite database.

## Features

- Add new tasks with a description, priority, and date.
- View all tasks sorted by date added, priority, and task ID.
- Update task descriptions, priorities, and dates.
- Delete tasks.
- Filter tasks by a specific date.

## Requirements

- Python 3.7 or later
- Streamlit
- SQLite3
- datetime

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/VIROOPAKSHC/To-Do-Stream.git
    ```

2. Install the required Python packages through the requirements.txt file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Code Overview

### Database Initialization

The SQLite database connection is initialized, and a table named `tasks` is created if it does not already exist.

### Functions

- `create_table()`: Creates the `tasks` table if it doesn't exist.
- `add_task(task, priority, date_added)`: Adds a new task to the database.
- `get_all_tasks()`: Retrieves all tasks from the database.
- `get_tasks_by_date(date_added)`: Retrieves tasks for a specific date from the database.
- `update_task(task_id, task, priority, date_added)`: Updates an existing task in the database.
- `delete_task(task_id)`: Deletes a task from the database.

### Streamlit App

- The app title is set using `st.title`.
- A form is created to add new tasks using `st.form`.
- All tasks are displayed with the ability to update or delete them.
- Tasks can be filtered by date using `st.date_input`.

## Example

![image](https://github.com/user-attachments/assets/518d75a0-d6c0-4dc1-84f5-849036608068)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

