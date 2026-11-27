"""Пример Python-программы для учебного задания по Git и GitHub."""


def greet(name):
    """Возвращает приветствие для переданного имени."""
    return f"Привет, {name}!"


def square(number):
    """Возвращает квадрат числа."""
    return number ** 2


if __name__ == "__main__":
    print(greet("мир"))
    print(f"Квадрат числа 5: {square(5)}")
