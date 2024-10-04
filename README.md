# manager_tasks_application

Это приложение управления задачами. Оно позволяет создавать, получать, обновлять и удалять задачи, а также управлять подзадачами.

## Установка

1. Клонируйте репозиторий
2. Убедитесь, что у вас установлен Python 3.11 или выше
3. Установите Poetry (если еще не установлен):

    ```bash
    pip install poetry

4. Установите зависимости:
    ```bash
    poetry install

## Запуск приложения

1.Запустите приложение с помощью Poetry:
    ```bash
    poetry run uvicorn bundle.main:app --host 0.0.0.0 --port 8000 --reload

2.После запуска приложение будет доступно по адресу http://127.0.0.1:8000

3. Документацию можно посмотреть по адресу http://127.0.0.1:8000/docs#/

