FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        return [task.strip() for task in tasks]

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def display_tasks(tasks):
    print("\nCurrent Tasks")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():

    tasks = load_tasks()

    while True:

        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            display_tasks(tasks)

            try:
                number = int(input("Task number to delete: "))
                tasks.pop(number - 1)
                save_tasks(tasks)
                print("Task deleted!")

            except:
                print("Invalid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
