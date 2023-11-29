import logging

import aiohttp
import requests


def error_during_api_access(url):
    logging.critical(f'Ошибка доступа к ADMIN API при чтении {url}')
    return {}


async def get_django_json(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    except Exception:
        return error_during_api_access(url)


def get_django_json_sync(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception:
        return error_during_api_access(url)
