tasks = [{'title': 'Sample Task', 'done': False}]

def remove_task(task):
    global tasks
    tasks = [t for t in tasks if t['title'] != task]
    return f"Задача '{task}' удалена"