import os
import datetime

# Define Task class
class Task:
    def __init__(self, task_id, title, description, status="Pending", due_date=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Status: {self.status}, Due Date: {self.due_date}, Description: {self.description}"

# File storage
TASKS_FILE = "tasks.txt"

# Helper functions
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                tasks.append(Task(*parts))
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task.task_id}|{task.title}|{task.description}|{task.status}|{task.due_date}\n")

def get_new_id(tasks):
    return str(len(tasks) + 1)

# CRUD operations
def add_task():
    tasks = load_tasks()
    task_id = get_new_id(tasks)
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    new_task = Task(task_id, title, description, "Pending", due_date)
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks():
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

def update_task():
    tasks = load_tasks()
    task_id = input("Enter task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            print("1. Update Status\n2. Update Details")
            choice = input("Enter choice: ")
            if choice == "1":
                new_status = input("Enter new status (Pending/Completed): ")
                task.status = new_status
            elif choice == "2":
                task.title = input("Enter new title: ")
                task.description = input("Enter new description: ")
                task.due_date = input("Enter new due date (YYYY-MM-DD): ")
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task():
    tasks = load_tasks()
    task_id = input("Enter task ID to delete: ")
    tasks = [task for task in tasks if task.task_id != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")

# Menu-driven interface
def main_menu():
    while True:
        print("\nTask Management Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
