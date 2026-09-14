from datetime import datetime


def validate_task_title(title: str):
    if title is None:
        raise ValueError("Task title cannot be None.")

    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")

    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    return True


def validate_task_description(description: str):
    if description is None:
        raise ValueError("Task description cannot be None.")

    if not isinstance(description, str):
        raise ValueError("Task description must be a string.")

    if not description.strip():
        raise ValueError("Task description cannot be empty.")
    if len(description) >500:
        raise ValueError("Desciption cannot be more than 500 chars long.")
    return True


def validate_due_date(due_date: str):
    if due_date is None:
        raise ValueError("Due date cannot be None.")

    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string.")

    if not due_date.strip():
        raise ValueError("Due date cannot be empty.")

    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            f"'{due_date}' is not a valid date. "
            "Expected format: YYYY-MM-DD."
        )

    return True
