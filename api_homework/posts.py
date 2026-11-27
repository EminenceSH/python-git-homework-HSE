"""Задание 1: GET-запрос и чтение JSON с первыми пятью постами."""

import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def main():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        posts = response.json()

        if not isinstance(posts, list):
            raise ValueError("Ожидался JSON-массив постов")

        for number, post in enumerate(posts[:5], start=1):
            print(f"Пост №{number}")
            print(f"Заголовок: {post['title']}")
            print(f"Текст: {post['body']}")
            print("-" * 40)

    except (requests.RequestException, ValueError, KeyError, TypeError):
        print("Не удалось получить или обработать список постов.")


if __name__ == "__main__":
    main()
