def validate_title(title):
    return isinstance(title, str) and len(title.strip()) > 0

if __name__ == "__main__":
    add_task("Study Git branches")
    add_task("Complete Lab 3")
    complete_task(1)
    print("Tasks:", list_tasks())

# Version 2.0 - Final
# Final review improvements added
