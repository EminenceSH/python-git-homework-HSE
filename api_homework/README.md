# Работа с HTTP API на Python

Примеры отправки GET-запросов с помощью библиотеки [`requests`](https://requests.readthedocs.io/), обработки JSON-ответов и передачи параметров в URL-запросах.

## Состав

| Файл | Описание |
| --- | --- |
| [`posts.py`](posts.py) | Загружает публикации из JSONPlaceholder и выводит заголовки и тексты первых пяти записей. |
| [`weather.py`](weather.py) | Получает текущую температуру и описание погоды по названию города через OpenWeather. |
| [`requirements.txt`](requirements.txt) | Список зависимостей проекта. |

## Подготовка окружения

Требуется Python 3 и доступ в интернет. Из корневой папки репозитория установите зависимости:

```bash
python -m pip install -r api_homework/requirements.txt
```

## Пример 1. Публикации JSONPlaceholder

Запуск:

```bash
python api_homework/posts.py
```

Скрипт выполняет запрос `GET https://jsonplaceholder.typicode.com/posts`, преобразует JSON-ответ в список объектов и выводит поля `title` и `body` первых пяти публикаций.

## Пример 2. Текущая погода OpenWeather

Для работы необходим действующий API-ключ сервиса [OpenWeather](https://openweathermap.org/api). Ключ передаётся через переменную окружения `OPENWEATHER_API_KEY`, а не хранится в исходном коде.

**Windows PowerShell**:

```powershell
$env:OPENWEATHER_API_KEY = "ВАШ_API_КЛЮЧ"
python api_homework/weather.py
```

**Linux / macOS**:

```bash
export OPENWEATHER_API_KEY="ВАШ_API_КЛЮЧ"
python api_homework/weather.py
```

Программа запрашивает название города и обращается к `GET https://api.openweathermap.org/data/2.5/weather` с параметрами:

| Параметр | Значение |
| --- | --- |
| `q` | Название города, введённое пользователем |
| `appid` | API-ключ из переменной окружения |
| `units` | `metric` — температура в °C |
| `lang` | `ru` — описание погоды на русском языке |

Пример формата вывода (фактические значения зависят от текущей погоды):

```text
Введите название города: Омск
Город: Omsk
Температура: 12.5 °C
Погода: облачно
```

Скрипт обрабатывает отсутствие API-ключа, ошибку авторизации, неизвестный город, превышение лимита запросов, сетевые ошибки и некорректные данные ответа.

## Используемые API

- [JSONPlaceholder — Posts](https://jsonplaceholder.typicode.com/)
- [OpenWeather — Current weather data](https://openweathermap.org/current)
