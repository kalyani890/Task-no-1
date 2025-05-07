import json
import os

TODO_FILE = "todo_data.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n Your to-do list is empty.")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input(" Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(" Task added.")
    else:
        print(" Task description cannot be empty.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input(" Enter task number to mark done/undone: ")) - 1
        tasks[index]["done"] = not tasks[index]["done"]
        print(" Task status updated.")
    except (ValueError, IndexError):
        print("️ Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input(" Enter task number to delete: ")) - 1
        deleted = tasks.pop(index)
        print(f" Deleted task: {deleted['title']}")
    except (ValueError, IndexError):
        print(" Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- ️ To-Do Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark done/undone")
        print("4. Delete task")
        print("5. Exit")

        choice = input(" Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(" Exiting... Tasks saved.")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

