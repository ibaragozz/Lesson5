all_tasks = []

class Task:
    def __init__(self, taskname, deadline, status=False):
        self.taskname = taskname
        self.deadline = deadline
        self.status = status

    @staticmethod
    def add_task(taskname, deadline, status=False):
        task = Task(taskname, deadline, status)
        all_tasks.append(task)

    @staticmethod
    def done(taskname):
        for task in all_tasks:
            if task.taskname == taskname:
                task.status = True
                break

    @staticmethod
    def show_tasks():
        for task in all_tasks:
            if not task.status:
                print(f'{task.taskname}, {task.deadline}')

# Получаем данные от пользователя
taskname = input("Введите название задачи: ")
deadline = input("Введите срок выполнения задачи (ДД:ММ:ГГГГ): ")

# Создаем и добавляем задачу
Task.add_task(taskname, deadline)

# Отображаем невыполненные задачи
print("Список невыполненных задач:")
Task.show_tasks()

# Пример завершения задачи
done_task = input("Введите название задачи, которую хотите пометить как выполненную: ")
Task.done(done_task)

# Отображаем оставшиеся невыполненные задачи
print("Оставшиеся невыполненные задачи:")
Task.show_tasks()
