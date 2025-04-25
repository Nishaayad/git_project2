tasks = []

def show_menu():
    print("\n----- To-Do List Menu -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"✅ Task added: '{task}'")

def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"❌ Task deleted: '{removed}'")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("👋 Exiting the app. Have a great day!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
