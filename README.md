# django-api-app

# Установка и настройка

**Установка**

Вы можете склонировать данное приложение:

```bash
git clone https://github.com/wultes/django-api-app
```

Или скачать его по этой [ссылке](https://github.com/wultes/django-api-app/archive/master.zip), а после распаковать его в удобном для вас месте.

Далее, нужно установить нужные библиотеки - это Django 2.2.7 и Rest Framework.

```bash
pip install -r requirements.txt
```

**Настройка**

Перейдите в каталог веб-приложения и создайте миграции.

```bash
cd django-api-app/main
python manage.py makemigrations app
python manage.py migrate
```

Также, вы можете создать супер-юзера, чтобы отслеживать корректность работы приложения. Это делается с помощью команды:

```bash
python manage.py makesuperuser
```

Теперь вы можете запускать сервер.

```bash
python manage.py runserver
```

### Работа веб-приложения

Изначально вы можете запутаться с тем, что делает веб приложение, поэтому здесь будет написано что делает каждая ссылка.

```url
admin/ - Переход в админку
api/all - Вывод всех созданных приложений
api/create - Создание приложения
api/detail/<id_app> - Вывод информации о приложении по ID
api/update/<id_app> - Редактирование приложенния по ID
api/test/<api_key> - Выводит всю информацию о приложении по API ключу
api/generate-api-key/<id_app> - Генерирует новый API ключ для приложения по его ID

Также, вы можете выводить некоторые ссылки в формате JSON
/api/all/?format=json - Вывод всех созданных приложений в формате JSON
/api/detail/<id_app>/?format=json - Вывод информации о приложении по ID в формате JSON
```


Теперь вы успешно можете пользоваться django-api-app.

### Лицензия

Copyright © 2020 [Wultes](https://github.com/wultes/).
