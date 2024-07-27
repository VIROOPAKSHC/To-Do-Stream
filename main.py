import streamlit as st
import sqlite3
from datetime import datetime

# Initialize connection to the SQLite database
conn = sqlite3.connect('todolist.db', check_same_thread=False)
c = conn.cursor()


# Create tasks table if it doesn't exist
def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            priority INTEGER,
            date_added DATE)
    ''')


def add_task(task, priority, date_added):
    c.execute(
        'INSERT INTO tasks (task, priority, date_added) VALUES (?, ?, ?)',
        (task, priority, date_added))
    conn.commit()


def get_all_tasks():
    c.execute(
        'SELECT * FROM tasks ORDER BY date_added DESC, priority DESC, id ASC')
    return c.fetchall()


def get_tasks_by_date(date_added):
    c.execute(
        'SELECT * FROM tasks WHERE date_added = ? ORDER BY priority DESC, id ASC',
        (date_added, ))
    return c.fetchall()


def update_task(task_id, task, priority, date_added):
    c.execute(
        'UPDATE tasks SET task = ?, priority = ?, date_added = ? WHERE id = ?',
        (task, priority, date_added, task_id))
    conn.commit()


def delete_task(task_id):
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id, ))
    conn.commit()


create_table()

# Title of the webpage
st.title(':orange[To-Do List] App')

with st.form("Add Task Form"):
    new_task = st.text_input(':green[Enter] Your Task')
    new_priority = st.number_input(
        ':red[Priority]', min_value=0, value=0, step=1,
        format='%d')  # Allow custom priority as an integer
    new_date_added = st.date_input(':gray[Date Added]', value=datetime.today())
    submitted = st.form_submit_button(':blue[Add Task]')
    if submitted and new_task:  # Check if a task description is provided
        add_task(new_task, new_priority, new_date_added.strftime('%Y-%m-%d'))

# Display current tasks
st.write(':green[All Tasks]:')
all_tasks = get_all_tasks()
for task in all_tasks:
    task_id, task_desc, task_priority, task_date_added = task
    col1, col2, col3, col4, col5 = st.columns([0.05, 0.5, 0.2, 0.15, 0.1])
    with col1:
        st.write(task_id)
    with col2:
        new_task_desc = st.text_area('',
                                     key=f'desc_{task_id}',
                                     value=task_desc,
                                     height=75)
    with col3:
        new_task_priority = st.number_input('',
                                            min_value=0,
                                            value=task_priority,
                                            step=1,
                                            format='%d',
                                            key=f'priority_{task_id}')
    with col4:
        new_task_date_added = st.date_input('',
                                            value=datetime.strptime(
                                                task_date_added, '%Y-%m-%d'),
                                            key=f'date_{task_id}')
    with col5:
        delete_button = st.button('Delete', key=f"delete_{task_id}")

    # Update the task if there is a change in task description, priority, or date
    if new_task_desc != task_desc or new_task_priority != task_priority or new_task_date_added != datetime.strptime(
            task_date_added, '%Y-%m-%d'):
        update_task(task_id, new_task_desc, new_task_priority,
                    new_task_date_added.strftime('%Y-%m-%d'))
    if delete_button:
        delete_task(task_id)
        st.experimental_rerun()

# Filter tasks by date
st.write('Tasks by Date:')
selected_date = st.date_input('Select a date to filter tasks',
                              value=datetime.today())
tasks_by_date = get_tasks_by_date(selected_date.strftime('%Y-%m-%d'))

# Display the tasks for the selected date
if tasks_by_date:
    for task in tasks_by_date:
        task_id, task_desc, task_priority, task_date_added = task
        st.write(
            f"ID: {task_id}, Description: {task_desc}, Priority: {task_priority}, Date Added: {task_date_added}"
        )
else:
    st.info('No tasks found for the selected date.')

# Close database connection when done
conn.close()
