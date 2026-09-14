from datetime import datetime


def validate_task_title(title: str):
    if title is None:
        print("Error: Task title cannot be None.")
        return False

    if not isinstance(title, str):
        print("Error: Task title must be a string.")
        return False

    if not title.strip():
        print("Error: Task title cannot be empty.")
        return False
    return True


def validate_task_description(description: str):
    if description is None:
        print("Error: Task description cannot be None.")
        return False

    if not isinstance(description, str):
        print("Error: Task description must be a string.")
        return False

    if not description.strip():
        print("Error: Task description cannot be empty.")
        return False
    return True


def validate_due_date(due_date: str):
    if due_date is None:
        print("Error: Due date cannot be None.")
        return False

    if not isinstance(due_date, str):
        print("Error: Due date must be a string.")
        return False

    if not due_date.strip():
        print("Error: Due date cannot be empty.")
        return False

    try:
        date = datetime.strptime(due_date.strip(), "%Y-%m-%d")

    except ValueError:
        print("Error: Invalid due date. Expected format: YYYY-MM-DD.")
        return False

    if date.date() < datetime.now().date():
        print("Error: Due date cannot be in the past.")
        return False

    return True