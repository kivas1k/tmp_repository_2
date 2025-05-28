from todo import add_task, remove_task, list_tasks, mark_done

print(add_task("Сделать домашку"))
print(add_task("Почитать книгу"))
print(mark_done("Сделать домашку"))
print(remove_task("Почитать книгу"))
print("\nСписок задач:")
print("\n".join(list_tasks()))