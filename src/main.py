APP_TITLE = "Python Task Manager"

tasks = []


def validate_title(title):
    return isinstance(title, str) and len(title.strip()) > 0


def add_task(title):
    if not validate_title(title):
        raise ValueError("Task title must be a non-empty string")
    task = {"id": len(tasks) + 1, "title": title.strip(), "done": False}
    tasks.append(task)
    return task


def list_tasks():
    return list(tasks)


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return True
    return False


def get_stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    active = total - completed
    return {"total": total, "completed": completed, "active": active}


if __name__ == "__main__":
    print(f"=== {APP_TITLE} ===")
    add_task("Study Git branches")
    add_task("Complete Lab 4")
    add_task("Review Pull Request")
    complete_task(1)
    print("Tasks:")
    for t in list_tasks():
        status = "Done" if t["done"] else "Active"
        print(f"  [{t['id']}] {t['title']} ({status})")
    stats = get_stats()
    print(f"Stats: total={stats['total']}, completed={stats['completed']}, active={stats['active']}")
