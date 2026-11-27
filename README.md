# Python: Git и HTTP API

Репозиторий с примерами программ на Python и историей работы с Git/GitHub. Проект включает простую консольную программу, блокнот Jupyter Notebook и примеры взаимодействия с публичными HTTP API.

## Структура проекта

| Файл или каталог | Описание |
| --- | --- |
| [`hello.py`](hello.py) | Приветствие и вычисление квадрата числа. |
| [`example.ipynb`](example.ipynb) | Блокнот Jupyter Notebook с примером выполнения Python-кода. |
| [`api_homework/`](api_homework/README.md) | Программы для GET-запросов, обработки JSON и получения погоды через API. |

## Требования

- Python 3
- Git — для клонирования репозитория
- Библиотека `requests` — для примеров с HTTP API

## Установка и запуск

Клонирование репозитория:

```bash
git clone https://github.com/EminenceSH/python-git-homework-HSE.git
cd python-git-homework-HSE
```

Запуск основной программы:

```bash
python hello.py
```

Вывод:

```text
Привет, мир!
Квадрат числа 5: 25
```

Для работы с HTTP API установите зависимости и запустите нужный скрипт:

```bash
python -m pip install -r api_homework/requirements.txt
python api_homework/posts.py
```

Получение погоды требует API-ключа OpenWeather. Настройка и запуск описаны в [документации к HTTP-примерам](api_homework/README.md).

## Jupyter Notebook

Блокнот [`example.ipynb`](example.ipynb) можно открыть локально в Jupyter Notebook или в [Google Colab](https://colab.research.google.com/github/EminenceSH/python-git-homework-HSE/blob/main/example.ipynb).

## История изменений

Разработка примера `hello.py` с добавлением функции возведения в квадрат выполнена в отдельной ветке и объединена с `main` через [Pull Request #1](https://github.com/EminenceSH/python-git-homework-HSE/pull/1).

Примеры работы с HTTP API добавлены через [Pull Request #2](https://github.com/EminenceSH/python-git-homework-HSE/pull/2).
