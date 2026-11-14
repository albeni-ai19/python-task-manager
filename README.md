# Python Task Manager

## Описание проекта
Консольное приложение на Python для управления списком задач. Проект разработан в рамках изучения систем контроля версий и предназначен для демонстрации работы с ветками Git, разрешения конфликтов слияния, оформления документации и работы с Pull Request на GitHub.

## Возможности
- Добавление новых задач с валидацией заголовка (`add_task`, `validate_title`).
- Просмотр списка всех задач и их текущего статуса (`list_tasks`).
- Отметка задачи как выполненной (`complete_task`).
- Удаление задачи по идентификатору (`delete_task`).
- Подсчёт статистики по задачам: всего, выполненных и активных (`get_stats`).
- Поиск и фильтрация задач по статусу (`src/search.py`).

## Технологии
| Технология / Инструмент | Версия | Назначение |
| --- | --- | --- |
| Python | 3.14 | Основной язык разработки приложения |
| Git | 2.53 | Распределённая система контроля версий |
| GitHub | — | Хостинг репозитория, Pull Request и Rulesets |
| venv / pip | встроенные | Изоляция окружения и проверка зависимостей |

## Структура проекта
```text
python-task-manager/
├── src/
│   ├── main.py
│   └── search.py
├── tests/
│   └── test_main.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Требования
- Операционная система Linux (Ubuntu), Windows или macOS.
- Установленный интерпретатор Python 3.10+ и система контроля версий Git.

## Установка
1. Клонируйте репозиторий с GitHub.
2. Перейдите в каталог проекта.
3. Создайте и активируйте виртуальное окружение.
4. Установите зависимости из файла `requirements.txt`.

```bash
git clone https://github.com/albeni-ai19/python-task-manager.git
cd python-task-manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
python3 src/main.py
```

## Использование
Пример вывода программы при запуске в терминале:
```text
=== Python Task Manager ===
Tasks:
  [1] Study Git branches (Done)
  [2] Complete Lab 4 (Active)
  [3] Review Pull Request (Active)
Stats: total=3, completed=1, active=2
```

## Зависимости
Проект использует только стандартную библиотеку Python и не требует установки сторонних пакетов. Список зависимостей зафиксирован в файле [requirements.txt](requirements.txt).

## Автор
Абельдинов Ильяс Ерланович, группа П-25-75б
