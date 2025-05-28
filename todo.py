tasks = []

def add_task(task):
    tasks.append({'title': task, 'done': False})
    return f"Задача '{task}' добавлена"