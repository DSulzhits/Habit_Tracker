Сервис полезных привычек. В проекте в качестве виртуального окружения используется Poetry.

1) После настройки виртуального окружения установите зависимости из файла pyproject.toml и заполните переменные
   окружения в файле .env, согласно шаблона .env.sample (кроме POSTGRESSQL_DB_NAME =), также в переменной REAL_EMAIL
   введите свой действующий email, этот адрес будет присвоен superuser (необходимо для работы функционала отправки
   письма при создании новой привычки)

2) Для создания базы данных выполните команду

```bash
psql -U <имя пользователя>
```

3) Создайте базу данных при помощи команды

```bash
CREATE DATABASE <имя базы данных> 
```

после чего занесите это имя в переменную окружения POSTGRESSQL_DB_NAME = ;

4) Выйдите из postgres при помощи команды

```bash
exit 
```

5) Создайте миграции командой

```bash
python manage.py makemigrations
```

Примените миграции при помощи команды

```bash
python manage.py migrate
```

6) Выполните команду для создания пользователей
```bash
python manage.py ccsu
```
7) Выполните команду для загрузки данных в базу при помощи фикстур
```bash
python manage.py loaddata data_habits.json
```
8) Запустите Redis при помощи терминала командой 
```bash
redis-server
```
он запустится на стандартном порте 6379.5.
Для проверки его работоспособности откройте 2-е окно терминала и выполните команду 
```bash
redis-cli ping
```
(если все в порядке ответ будет "pong")

9) Запустите Celery 
```bash
celery -A habit_tracker worker -l INFO
```
```bash
celery -A habit_tracker beat -l info
```


Модели
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка
не должна расходовать на выполнение больше 2 минут. Исходя из этого получаем первую модель — Привычка.

Привычка:
- Пользователь — создатель привычки.
- Место — место, в котором необходимо выполнять привычку.
- Время — время, когда необходимо выполнять привычку.
- Действие — действие, которое представляет из себя привычка.
- Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для
приятных.
- Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
- Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
- Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
- Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие
привычки.

Обратите внимание, что в проекте у вас может быть больше, чем одна описанная здесь модель.

Валидаторы
- Исключить одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.


Пагинация
- Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.


Права доступа
- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

Эндпоинты
- Регистрация
- Авторизация
- Список привычек текущего пользователя с пагинацией
- Список публичных привычек
- Создание привычки
- Редактирование привычки
- Удаление привычки
- Интеграция

Для полноценной работы сервиса необходим реализовать работу с отложенными задачами для напоминания о том, в какое время
какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Telegram, который будет заниматься рассылкой уведомлений.
Для создания Telegram-бота найдите в чате самого главного бота: https://t.me/BotFather.
Начните с ним диалог и выберите команду создания нового бота:

BotFather предложит ввести имя вашего бота:

Здесь нужно указать видимое имя бота, т. е. то, которое отображается пользователям. Например, OlegHabbitBot.

После этого BotFather спросит юзернейм вашего бота.

Здесь бота нужно назвать уникально — это тот уникальный идентификатор, по которому бота можно будет найти. Также важно,
чтобы имя заканчивалось на _bot.

Например,
oleg_habbit_bot
.

Если имя подходит под все правила, BotFather предоставит токен и полезные ссылки для использования бота:

Токен будет использован ботом для обращения к API Telegram-сервисов, поэтому его необходимо сразу сохранить и не
распространять.

Безопасность
- Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

Документация
- Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. При необходимости
эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную.