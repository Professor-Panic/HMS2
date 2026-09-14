from datetime import datetime

# Import validation functions
from task_manager.validation import *

# Define tasks list
tasks = [
    {
        "title": "Groceries",
        "description": "Shop at Market Basket for food",
        "due_date": "2024-06-26",
        "completed": True
    }
]


# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    tasks[index]["completed"] = True
    print("Task marked as complete!")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for task in tasks:
        if task["completed"] == False:
            print(task)


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    progress = 0
    for task in tasks:
        if task["completed"] == True:
            progress += 1
    if len(tasks) == 0:
        return 0
    progress = (progress / len(tasks))*100 #I'll show progress in percentage
    return progress