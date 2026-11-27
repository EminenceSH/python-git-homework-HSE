"""Задание 2: получение текущей температуры и погоды через OpenWeather."""

import os

import requests


URL = "https://api.openweathermap.org/data/2.5/weather"


def main():
    city = input("Введите название города: ").strip()
    if not city:
        print("Название города не может быть пустым.")
        return

    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        print("Сначала задайте переменную окружения OPENWEATHER_API_KEY.")
        return

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Город: {data.get('name', city)}")
        print(f"Температура: {temperature} °C")
        print(f"Погода: {description}")

    except requests.HTTPError as error:
        code = error.response.status_code if error.response is not None else None
        if code == 401:
            print("Неверный API-ключ OpenWeather или ключ ещё не активирован.")
        elif code == 404:
            print("Город не найден. Проверьте написание.")
        elif code == 429:
            print("Превышен лимит запросов OpenWeather.")
        else:
            print(f"Ошибка ответа API (HTTP {code}).")
    except requests.RequestException:
        print("Сетевая ошибка при обращении к OpenWeather.")
    except (ValueError, KeyError, IndexError, TypeError):
        print("Не удалось обработать JSON-ответ OpenWeather.")


if __name__ == "__main__":
    main()
