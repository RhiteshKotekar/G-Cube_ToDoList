# Program for a To-Do List

# Rhitesh R Kotekar


def AddTasks():
    ### Program to add tasks
    repeatNum = int(input("\nHow many tasks?: "))
    for i in range(repeatNum):
        task = input("Enter task: ")
        taskslst.append({"task": task, "done": False})
        print("Task added!")


def reviewTasks():
    ### Program to display all the current tasks
    print("\nTasks:")
    for i, task in enumerate(taskslst):
        status = "X" if task["done"] else "O"
        print(f"{i + 1}. {task['task']} - {status}")


def markTask():
    ### Program to mark task as done
    reviewTasks()
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(taskslst):
        taskslst[task_num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number!")


def deleteTask():
    ### Program to delete task
    reviewTasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(taskslst):
        removed_task = taskslst.pop(task_num)
        print(f"Task '{removed_task['task']}' deleted!")
    else:
        print("Invalid task number!")


taskslst = []

while True:
    ## To-Do List Operations
    oper = [
        "Add Task",
        "Show Tasks",
        "Mark Task as Done",
        "Delete a Task",
        "Exit",
    ]

    print("\nWelcome to To-Do List")
    for i, option in enumerate(oper):
        print(f"{i + 1}. {option}")

    choice = input("So, What do you wish to do? :  ")

    if choice == "1":
        AddTasks()
    elif choice == "2":
        reviewTasks()
    elif choice == "3":
        markTask()
    elif choice == "4":
        deleteTask()
    elif choice == "5":
        print("Good Luck completing those tasks!")
        break
    else:
        print("Hmm... Check that option once again..")
