# Python Git Homework — HSE

Учебный репозиторий для отработки работы с **Git** и **GitHub**: создание репозитория, клонирование на компьютер, создание ветки, коммиты, Pull Request и слияние с основной веткой `main`.

## Содержимое

- `hello.py` — простая программа на Python: выводит приветствие; в дополнительной ветке реализована функция возведения числа в квадрат.
- `example.ipynb` — блокнот Jupyter Notebook для запуска через Google Colab.

## Запуск на компьютере

Необходим Python 3.

```bash
git clone https://github.com/EminenceSH/python-git-homework-HSE.git
cd python-git-homework-HSE
python hello.py
```

После слияния Pull Request программа выводит:

```text
Привет, мир!
Квадрат числа 5: 25
```

## Запуск в Google Colab

Откройте [Google Colab](https://colab.research.google.com/), выберите **GitHub**, найдите репозиторий `EminenceSH/python-git-homework-HSE` и откройте `example.ipynb`. Запустите ячейку с кодом.

## Практика работы с ветками

1. Клонировать репозиторий.
2. Создать ветку `feature/add-square`.
3. Изменить `hello.py`, добавив функцию `square()`.
4. Отправить ветку в GitHub и создать Pull Request в `main`.
5. Объединить изменения с `main`.

Список завершённых Pull Request можно проверить во вкладке **Pull requests → Closed**.
