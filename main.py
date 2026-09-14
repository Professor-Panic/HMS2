import task_manager.task_utils as task_utils

# Define the main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            task_utils.add_task(title, description, due_date)

        elif choice == "2":
            if len(task_utils.tasks) == 0:
                print("There are no tasks.")
                continue

            print("\nTasks:")
            #print all pending tasks
            for index, task in enumerate(task_utils.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} - {status}")

            try:
                index = int(input("Enter the task number to mark as complete: "))
                if index < 0 or index >= len(task_utils.tasks):
                    print("Invalid task number.")
                    continue

                task_utils.mark_task_as_complete(index)

            except ValueError:
                print("Please enter a valid task number.")

        elif choice == "3":
            print("\nPending Tasks:")
            task_utils.view_pending_tasks()

        elif choice == "4":
            progress = task_utils.calculate_progress()
            print(f"\nProgress: {progress:.1f}%")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()