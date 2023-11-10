![workflow](https://github.com/Studio-Yandex-Practicum/vtoroe_dyhanie/actions/workflows/vtoroe_dyhanie_develop.yml/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit-hooks/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit-hooks/main)

## <img src='https://shop.vtoroe.ru/wp-content/themes/cshops/assets/img/favicon.ico'/> vtoroe_dyhanie (Второе дыхание)

Проект телеграм-бота для новых и действующих сотрудников Фонда "Второе дыхание". Помогает автоматизировать HR-процессы и позволяет новым сотрудникам быстрее адаптироваться за счет автоматизации предоставления необходимой информации о работе Фонда.

<details>
<summary>Задачи бота</summary>

- Оптимизация процесса онбординга для новых коллег Фонда "Второе дыхание"
- Сокращение рабочего времени hr на ответы на одинаковые вопросы коллег
- Контроль эмоционального состояния коллег
- Сбор аналитики

</details>

<details>
<summary>Функции бота</summary>

- Предоставление информации о Фонде (общая, ссылка на сайт)
- Предоставление общей информации о проекте (адрес, директор, оргструктура)
- Ответы на часто задаваемые вопросы
- Помощь с документами и формами (присылать документ по выбору из меню)
- Собирает информацию для аналитики
- Отложенное отправление напоминаний для конкретных сотрудников
- Периодический опрос о самочувствии сотрудников
</details>

<details>
<summary>Возможности бота для новых сотрудников</summary>

- Предоставление необходимой информации, ресурсы
- Ответы на вопросы
- Кадровые документы
- Напоминания
</details>

<details>
<summary>Stack</summary>

- Python 3.11
- Python-telegram-bot 20.5
- Docker
- Docker-Compose
- Poetry 1.6.1
</details>

<details>
<summary>Установка и запуск проекта</summary>

Клонируйте репозиторий:

```
git clone git@github.com:Studio-Yandex-Practicum/vtoroe_dyhanie.git
```

Перейдите в директорию проекта:

```
cd vtoroe_dyhanie/
```

Инициализируйте создание директории виртуального окружения в проекте:

```
poetry config virtualenvs.in-project true
```

Создайте директорию виртуального окружения:

```
poetry install
```

Далее вы можете либо запустить виртуальное окружение самостоятельно:

```
poetry shell
```

Или воспользовавшись вот такой командой:

```
source .venv/bin/activate (для UNIX)
source .venv/Scripts/activate (для WINDOWS)
```

Создайте в корневой папке проекта файл .env и заполни данные по шаблону:

```
TELEGRAM_TOKEN='<здесь ваш токен>'
SMTP_SERVER='<smtp сервер>'
PORT='<SSL подключения>'
SENDER_EMAIL='<Емайл отправителя>'
RECEIVER_EMAIL='<Емайл получателя>'
PASSWORD_EMAIL='<Пароль от Емайл отправителя>'
```

Запустите проект локально, чтобы проверить работоспособность:

```
python src\application.py
```

</details>

<details>
<summary>Команда разработки</summary>

Тимлид:

- [Яна Денисова](https://github.com/Yana-Denisova)

Проджект менеджер:

- [Татьяна Кумова](https://github.com/kmvtn)

Разработчики:

- [Александр Мамонов](https://github.com/Alex386386)
- [Владимир Максимов](https://github.com/v-mcsimoff)
- [Андрей Мольков](https://github.com/MrProfessorCat)
- [Дмитрий Насибуллин](https://github.com/IlDezmond)
- [Андрей Киланов](https://github.com/AndyFebruary74)
- [Мария Ковалева](https://github.com/Maria50538810)
- [Виктория Латышева](https://github.com/vikkilat)
- [Евгений Квас](https://github.com/Leon6565)
- [Анастасия Савельева](https://github.com/Esperansa08)
- [Настасья Мартынова](https://github.com/Nastasya-M)
- [Евгений Голодных](https://github.com/Evgeniy-Golodnykh)
- [Дмитрий Корепанов](https://github.com/DNKer)
- [Михаил Волков](https://github.com/greenpandorik)
- [Евгений Коваленко](https://github.com/evgeny-dmitrievich)
- [Александр Новожилов](https://github.com/AleksNovo)
- [Олег Исаев](https://github.com/oisaev)
- [Дмитрий Белолипецкий](https://github.com/EvolDem)

</details>
