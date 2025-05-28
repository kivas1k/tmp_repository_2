from todo import add_task, remove_task, list_tasks, mark_done

def main():
    while True:
        print("\nToDo App: 1. Добавить задачу 2. Удалить задачу 3. Отметить выполненной 4. Показать задачи 5. Выход")
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            task = input("Введите задачу: ")
            print(add_task(task))
        elif choice == "2":
            task = input("Введите задачу для удаления: ")
            print(remove_task(task))
        elif choice == "3":
            task = input("Введите задачу для отметки как выполненной: ")
            print(mark_done(task))
        elif choice == "4":
            print("\nСписок задач:")
            print("\n".join(list_tasks()))
        elif choice == "5":
            print("Выход")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()