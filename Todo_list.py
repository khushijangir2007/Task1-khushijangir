#task1- to do list 
tasks = []
print("To-Do List")
while True:
    task = input("Enter a task (or type done to stop): ")
    if task.lower() == "done":
        break
    tasks.append(task)

print("\nMy Tasks:")
for i, task in enumerate(tasks, 1):
    print(i, task)
