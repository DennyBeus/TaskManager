def add_task(text):
    tasks[len(tasks) + 1] = {'task': text, 'done': False}

def status_task(status):
    if tasks[status]['done'] == False:
        change_status = True
    else:
        change_status = False
    tasks[status]['done'] = change_status

def del_task(number):
    if number == len(tasks):
        del tasks[number]
    else:
        del tasks[number]
        for i in range(len(tasks) + 1 - number):
            tasks[number + i] = tasks[number + i + 1]
        del tasks[len(tasks)]

tasks = {}

menu_buttons = [['1 - Добавить задачу', '2 - Изменить статус задачи'], 
                ['3 - Удалить задачу', '4 - Показать все задачи'], 
                ['5 - Показать активные задачи', '6 - Выполненные задачи']]

filter_mode = 'all'

while True:
    print('Менеджер задач:')
    print('-' * 56)
    if tasks == {}:
        print('Список задач пуст')
    for i in range(len(tasks)):
        if filter_mode == 'active' and tasks[i + 1]['done']:
            continue
        if filter_mode == 'done' and not tasks[i + 1]['done']:
            continue
        symbol = '✓' if tasks[i + 1]['done'] else ' '
        print(f'{i + 1} - [{symbol}] - {tasks[i + 1]['task']}')
    print('-' * 56)
    for row in menu_buttons:
        for elem in row:
            print(str(elem).ljust(30), end='')
        print()
    print('Напишите "exit" для выхода из программы')
    answer = input()
    if answer == 'exit':
        break
    try:
        answer_num = int(answer)
    except ValueError:
        print('* Введите число! *')
        continue
    if answer_num == 1:
        task_text = input('Опишите задачу: ')
        add_task(task_text)
    if answer_num == 2:
        try:
            status = int(input('Укажите номер задачи: '))
            if status > len(tasks):
                print('* Задачи с таким номером нет! *')
                continue
        except ValueError:
            print('* Введите число! *')
            continue
        status_task(status)
    if answer_num == 3:
        try:
            number = int(input('Укажите номер задачи: '))
            if number > len(tasks):
                print('* Задачи с таким номером нет! *')
                continue
        except ValueError:
            print('* Введите число! *')
            continue
        del_task(number)
    if answer_num == 4:
        filter_mode = 'all'
    if answer_num == 5:
        filter_mode = 'active'
    if answer_num == 6:
        filter_mode = 'done'
        