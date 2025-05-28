tasks = []

def add_task(task):
    tasks.append({'title': task, 'done': False})
    return f"Задача '{task}' добавлена"

def remove_task(task):
    global tasks
    tasks = [t for t in tasks if t['title'] != task]
    return f"Задача '{task}' удалена"