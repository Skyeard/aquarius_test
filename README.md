# Тестовое задание. Сетевое тестирование (pyATS)

## Описание проекта

Автоматизированные тесты для сетевых устройств (коммутаторы, роутеры) на **pyATS** фреймворке.


## Быстрый запуск

### Задание 1: Ручное тестирование
```bash
python manual_testing.py
```

### Задание 2: Автоматические тесты
```bash
# 1. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Linux

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Запустить тест-модули
python -m tests.test_network_device
python -m tests.test_router  
python -m tests.test_switch
```