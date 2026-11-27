# Домашняя работа: GET-запросы и JSON

Оба задания реализованы на Python с использованием библиотеки [`requests`](https://requests.readthedocs.io/).

## Содержание

| Файл | Назначение |
| --- | --- |
| `posts.py` | Отправляет GET-запрос к `https://jsonplaceholder.typicode.com/posts`, разбирает JSON, выводит заголовки и тексты первых 5 постов. |
| `weather.py` | Спрашивает город, отправляет GET-запрос к OpenWeather с параметрами, выводит температуру в °C и описание погоды. |
| `requirements.txt` | Зависимость `requests`. |

## Как запустить

Из корня репозитория:

```bash
python -m pip install -r api_homework/requirements.txt
python api_homework/posts.py
```

Для второй задачи нужен **личный API-ключ OpenWeather**. Зарегистрируйтесь на [OpenWeather](https://openweathermap.org/api), найдите API key в личном кабинете. Не добавляйте ключ в код или GitHub.

**Windows PowerShell** — установить переменную окружения для текущего терминала:

```powershell
$env:OPENWEATHER_API_KEY = "ВАШ_API_КЛЮЧ"
python api_homework/weather.py
```

**Linux / macOS**:

```bash
export OPENWEATHER_API_KEY="ВАШ_API_КЛЮЧ"
python api_homework/weather.py
```

Программа попросит название города (например, `Омск`), отправит запрос к `https://api.openweathermap.org/data/2.5/weather` с параметрами:

- `q`: введённое название города;
- `appid`: ключ из `OPENWEATHER_API_KEY`;
- `units=metric`: температура в градусах Цельсия;
- `lang=ru`: описание погоды на русском.

Ожидаемый формат вывода (числа и погодные условия зависят от фактического ответа API):

```text
Введите название города: Омск
Город: Omsk
Температура: <текущее значение> °C
Погода: <описание>
```

Обрабатываются сетевые ошибки, отсутствие ключа, неверный ключ (401), неизвестный город (404), превышение лимита (429) и некорректный JSON.

## Соответствие критериям

- [x] **Задание 1:** GET `/posts`, разбор JSON и печать заголовка и тела первых пяти постов.
- [x] **Задание 2:** ввод названия города, GET к OpenWeather с параметрами, вывод температуры и описания погоды (при наличии действующего API-ключа).

## Документация API

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- [OpenWeather — Current weather data](https://openweathermap.org/api/current)
