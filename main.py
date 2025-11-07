def add_task(text):
    tasks[len(tasks) + 1] = {'task': text, 'done': False}

def status_task(status):
    if tasks[status]['done'] == False:
        change_status = True
    else:
        change_status = False
    tasks[status]['done'] = change_status

def del_task(number):
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
    if filter_mode == 'active': 
        for i in range(len(tasks)):
            if tasks[i + 1]['done'] == False:
                print(f'{i + 1} - [ ] - {tasks[i + 1]['task']}')
    if filter_mode == 'done':
        for i in range(len(tasks)):
            if tasks[i + 1]['done'] == True:
                print(f'{i + 1} - [✓] - {tasks[i + 1]['task']}')
    if filter_mode == 'all':
        if tasks == {}:
            print('У вас пока нет задач')
        else:
            for i in range(len(tasks)):
                if tasks[i + 1]['done'] == True:
                    symbol = '✓'
                else:
                    symbol = ' '
                print(f'{i + 1} - [{symbol}] - {tasks[i + 1]['task']}')
    print('-' * 56)
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
        status = int(input('Укажите номер задачи: '))
        status_task(status)
    if int(answer) == 3:
        number = int(input('Укажите номер задачи: '))
        del_task(number)
    if int(answer) == 4:
        filter_mode = 'all'
    if int(answer) == 5:
        filter_mode = 'active'
    if int(answer) == 6:
        filter_mode = 'done'
    if answer == 'exit':
        break
        


