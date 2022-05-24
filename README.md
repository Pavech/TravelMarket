# TravelMarket

![TeamCity build status](http://188.120.227.87:8111/app/rest/builds/buildType:id:TravelMarket_2_BuildPavelTravelMarket/statusIcon.svg) [![Python application](https://github.com/Pavech/TravelMarket/actions/workflows/python-app.yml/badge.svg)](https://github.com/Pavech/TravelMarket/actions/workflows/python-app.yml)

Итоговый проект:

Цель: Автоматизация тестирования UI

Задачи:

 • Написание автотестов

 • Настройка и запуск тестов в CI

 • Написание тест кейсов

 • Получение отчетов по результатам тестирования

Набор технологий:

 • Python

 • Pytest

 • Selenium

Web application:
```angular2html
https://cypress-tourism-app.herokuapp.com
```
Create virtual environment:

```angular2html
python3 -m venv env
```

Activate virtual environment:
```angular2html
source env/bin/activate
```

Install requirements:

```angular2html
pip3 install -r requirements.txt
```

Run tests:

```angular2html
pytest
```

Logging

```angular2html
https://docs.python.org/3/library/logging.html
```

Code review

```angular2html
https://pre-commit.com/
```

Test results

```angular2html
https://docs.qameta.io/allure/
```

### План работы:
- Необходимо написать ui тесты на https://cypress-tourism-app.herokuapp.com
- Необходимо написать тесты на  3 раздела (авторизация, регистрация и бронирование отеля). Для каждого раздела необходимо добавить позитивные и негативные тесты (количество на выбор студента). Для раздела бронирования достаточно позитивного теста.
- Необходимо составить к тестам тестовую документацию. В тест кейсах должны быть предварительные шаги (если это необходимо), шаги, ожидаемый результат. Как и где ее хранить остается на выбор студента.

### Требования:
- [x] README.md заполнен и содержит актуальную информацию
- [x] В файле README.md присутствуют бейджики CI
- [x] В файле README.md инструкция по установке зависимостей и запуску тестов
- [x] Необходимо настроить CI. В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с CI.
- [x] Необходимо настроить линтер, который должен запускаться локально/на стороне CI
- [x] К каждому тесту должны присутствовать тест кейсы
