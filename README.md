# Проект выпускной дипломной работы курса "Python-разработчик" на платформе Практикум от Яндекс.   
# Проект - FoodGram http://158.160.8.21/

![статус сборки](https://github.com/MikhailGolovin1982/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?event=push)

## Проект FoodGram «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Сервисы и страницы проекта
Посмотрите сайт проекта http://158.160.8.21/

### Главная страница
Содержимое главной страницы — список первых шести рецептов, отсортированных по дате публикации (от новых к старым). Остальные рецепты доступны на следующих страницах: внизу страницы есть пагинация.

### Страница рецепта
На странице — полное описание рецепта. Для авторизованных пользователей — возможность добавить рецепт в избранное и в список покупок, возможность подписаться на автора рецепта.

### Страница пользователя
На странице — имя пользователя, все рецепты, опубликованные пользователем и возможность подписаться на пользователя.

### Подписка на авторов
Подписка на публикации доступна только авторизованному пользователю. Страница подписок доступна только владельцу.
Сценарий поведения пользователя:
1. Пользователь переходит на страницу другого пользователя или на страницу рецепта и подписывается на публикации автора кликом по кнопке «Подписаться на автора».
2. Пользователь переходит на страницу «Мои подписки» и просматривает список рецептов, опубликованных теми авторами, на которых он подписался. Сортировка записей — по дате публикации (от новых к старым).
3. При необходимости пользователь может отказаться от подписки на автора: переходит на страницу автора или на страницу его рецепта и нажимает «Отписаться от автора».

### Список избранного
Работа со списком избранного доступна только авторизованному пользователю. Список избранного может просматривать только его владелец.
Сценарий поведения пользователя:
1. Пользователь отмечает один или несколько рецептов кликом по кнопке «Добавить в избранное».
2. Пользователь переходит на страницу «Список избранного» и просматривает персональный список избранных рецептов.
3. При необходимости пользователь может удалить рецепт из избранного.

### Список покупок
Работа со списком покупок доступна авторизованным пользователям. Список покупок может просматривать только его владелец.
Сценарий поведения пользователя:
1. Пользователь отмечает один или несколько рецептов кликом по кнопке «Добавить в покупки».
2. Пользователь переходит на страницу Список покупок, там доступны все добавленные в список рецепты. Пользователь нажимает кнопку Скачать список и получает файл с суммированным перечнем и количеством необходимых ингредиентов для всех рецептов, сохранённых в «Списке покупок».
3. При необходимости пользователь может удалить рецепт из списка покупок.
Список покупок скачивается в формате PDF.
При скачивании списка покупок ингредиенты в результирующем списке не должны дублироваться; если в двух рецептах есть сахар (в одном рецепте 5 г, в другом — 10 г), то в списке должен быть один пункт: Сахар — 15 г.
В результате список покупок может выглядеть так:
- Фарш (баранина и говядина) (г) — 600
- Сыр плавленый (г) — 200
- Лук репчатый (г) — 50
- Картофель (г) — 1000
- Молоко (мл) — 250
- Яйцо куриное (шт) — 5
- Соевый соус (ст. л.) — 8
- Сахар (г) — 230
- Растительное масло рафинированное (ст. л.) — 2
- Соль (по вкусу) — 4
- Перец черный (щепотка) — 3

### Фильтрация по тегам
При нажатии на название тега выводится список рецептов, отмеченных этим тегом. Фильтрация может проводится по нескольким тегам в комбинации «или»: если выбраны несколько тегов — в результате должны быть показаны рецепты, которые отмечены хотя бы одним из этих тегов.
При фильтрации на странице пользователя должны фильтроваться только рецепты выбранного пользователя. Такой же принцип должен соблюдаться при фильтрации списка избранного.

### Регистрация и авторизация
В проекте должна быть доступна система регистрации и авторизации пользователей. Чтобы собрать весь код для управления пользователями воедино — создайте приложение users.

#### Обязательные поля для пользователя:
- Логин
- Пароль
- Email
- Имя
- Фамилия

#### Уровни доступа пользователей:
- Гость (неавторизованный пользователь)
- Авторизованный пользователь
- Администратор

### Что могут делать неавторизованные пользователи
- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.

### Что могут делать авторизованные пользователи
- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Как запустить проект (режим демонстрации - в Docker - контейнерах). 
Для простоты развертывания и демонтсрации, проект подготовлен для автоматического разворачивания в четырёхы докер-контейнерах. 
- nginx 
- backend 
- frontend
- db

### Последовательность разворачивания проекта. 
1) Клонировать репозиторий командой: 
```bash 
git clone git@github.com:MikhailGolovin1982/foodgram-project-react.git 
``` 
2) Если на вашем ПК не установлено прилоджение Docker Desktop - [скачайте и установите его] (https://www.docker.com/products/docker-desktop/)
   
(должна быть настроена система виртуализации на вашем ПК, в вашей операционной системе)

3) Перейдите в папку  
```bash 
cd foodgram-project-react/infra/ 
```
4) Выполните в терминале команду  
```bash 
docker-compose up 
```
В результате выполнения данной команды в вашем приложении Docker Desktop появиться четыре образа: 
- backend
- frontend
- nginx  
- db

5) Выполнить миграции командой: 
```bash 
docker-compose exec web python manage.py migrate 
``` 

6) Создать суперпользователя 
```bash 
docker-compose exec web python manage.py createsuperuser 
``` 

7) Собрать статику: 
```bash     
docker-compose exec web python manage.py collectstatic --no-input 
``` 

8) Теперь проект доступен по адресу: 
     http://localhost/admin/  
     можно зайти по данной ссылке на сайт, создать необходимые записи, проверить работу API, например через PostMan

9) Подробное описание API интрефейса приведено на страничке: 
   http://localhost/api/redoc/ 

####   Например
   Алгоритм регистрации пользователей
- Пользователь отправляет POST-запрос на добавление нового пользователя с обязательными параметрами на эндпоинт
 /api/users/
в формате json:
```json
{
    "email": "user@mmm.ru",
    "username": "user",
    "first_name": "user_first_name",
    "last_name": "user_last_name",
    "password": "user_12345"
}
```
- Пользователь отправляет POST-запрос с параметрами email и password на эндпоинт /api/auth/token/login
в ответе на запрос ему приходит token 
Более подробная информация приведена в документации  http://localhos/api/redoc/

11) Рекомендуется создать копию базы данных командой: 
```bash 
docker-compose exec backends python manage.py dumpdata > fixtures.json 
``` 
## Описание переменных окружения 

### Переменные окружения содержатся в файле .env 
``` 
DB_ENGINE = <Тип базы данных - postgresql>  
DB_NAME = <имя базы данных> 
POSTGRES_USER = <логин для подключения к базе данных> 
POSTGRES_PASSWORD = <пароль для подключения к БД> 
DB_HOST = <название сервиса (контейнера), 'db'> 
DB_PORT = <порт для подключения к БД, 5432> 
SECRET_KEY = <секретный ключ> 
DEBUG = <состояние режима отладки, False> 
ALLOWED_HOSTS = <разрешенные хосты- '*', 127.0.0.1> 
```  

### Заполнение базы данных ингредиентами
Для заполнения базы данных ингредиентами используется файл
```
/foodgram-project-react/backend/data/ingredients.csv
```
Для заполнения базы данных используется команда:
```bash
./manage.py upload_ingredients
```
файл с данными (ingredients.csv) предварительно скопируйте в папку с файлом manage.py 

### Автор проекта:  
- Михаил Головин 
