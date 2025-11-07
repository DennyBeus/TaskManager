def add_task(text):
    tasks[len(tasks) + 1] = {'task': task_text, 'done': False}

def status_task(status):
    if tasks[status]['done'] == False:
        change_status = True
    else:
        change_status = False
    tasks[status] = {'done': change_status}
    
tasks = {}

menu_buttons = [['1 - Добавить задачу', '2 - Отметить задачу выполненной'], 
                ['3 - Удалить задачу', '4 - Показать все задачи'], 
                ['5 - Показать активные задачи', '6 - Выполненные задачи']]

while True:
    print('Менеджер задач:')
    print('-' * 61)
    for row in menu_buttons:
        for elem in row:
            print(str(elem).ljust(30), end='')
        print()
    print('Напишите "exit" для выхода из программы')
    answer = input()
    if int(answer) == 1:
        task_text = input('Опишите задачу: ')
        add_task(task_text)
    if int(answer) == 2:
        status = input('Укажите номер задачи: ')
        status_task(status)

