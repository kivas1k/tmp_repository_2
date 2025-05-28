tasks = []

def add_task(task):
    tasks.append({'title': task, 'done': False})
    return f"Задача '{task}' добавлена"

def remove_task(task):
    global tasks
    tasks = [t for t in tasks if t['title'] != task]
    return f"Задача '{task}' удалена"

def list_tasks():
    return [f"[{'x' if t['done'] else ' '}] {t['title']}" for t in tasks]

def mark_done(task):
    for t in tasks:
        if t['title'] == task:
            t['done'] = True
            return f"Задача '{task}' отмечена как выполненная"
    return f"Задача '{task}' не найдена"