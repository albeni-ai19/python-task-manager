from src.main import tasks, add_task, list_tasks, complete_task

def test_task_manager():
    tasks.clear()
    t = add_task(Test task)
    assert len(list_tasks()) == 1
    assert complete_task(t[id]) is True
