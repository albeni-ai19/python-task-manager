tasks = []

def add_task(title):
    task = {id: len(tasks) + 1, title: title, done: False}
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def complete_task(task_id):
    for task in tasks:
        if task[id] == task_id:
            task[done] = True
            return True
    return False

if __name__ == __main__:
    add_task(Study Git branches)
    add_task(Complete Lab 3)
    complete_task(1)
    print(Tasks:, list_tasks())

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t[id] != task_id]

def validate_title(title):
    return isinstance(title, str) and len(title.strip()) > 0
# Version 1.1
