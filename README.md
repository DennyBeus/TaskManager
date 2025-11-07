# Task Manager

A simple command-line task manager in Python with filtering capabilities.

## Features

- Add tasks with completion status
- Toggle task status (done/not done)
- Delete tasks with automatic renumbering
- Filter tasks by status (all/active/completed)
- Input validation and error handling

## Usage

Run the program:
```
python main.py
```

Select an option from the menu (1-6) or type 'exit' to quit.

## Example
```
Менеджер задач:
--------------------------------------------------------
1 - [ ] - Купить молоко
2 - [✓] - Написать отчет
3 - [ ] - Позвонить врачу
--------------------------------------------------------
1 - Добавить задачу           2 - Изменить статус задачи
3 - Удалить задачу            4 - Показать все задачи
5 - Показать активные задачи  6 - Выполненные задачи
Напишите "exit" для выхода из программы
```

## Filtering

- Option 4: Show all tasks
- Option 5: Show only active tasks
- Option 6: Show only completed tasks
