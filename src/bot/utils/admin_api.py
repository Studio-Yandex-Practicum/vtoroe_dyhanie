import logging

import aiohttp
import requests

from bot.core.settings import api_root

async_session: aiohttp.ClientSession = None
sync_session: requests.Session = None


def get_sync_session():
    global sync_session
    if sync_session:
        return sync_session
    return requests.Session()


async def get_async_session():
    global async_session
    if async_session and not async_session.closed:
        return async_session
    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            keepalive_timeout=24 * 3600),
    )


def error_during_api_access(url):
    logging.critical('Ошибка доступа к ADMIN API '
                     f'при чтении {api_root}/{url}')
    return {}


async def get_django_json(url):
    try:
        global async_session
        async_session = await get_async_session()
        async with async_session.get(f'{api_root}/{url}') as response:
            return await response.json()
    except Exception:
        return error_during_api_access(url)


def get_django_json_sync(url):
    try:
        global sync_session
        sync_session = get_sync_session()
        with sync_session.get(f'{api_root}/{url}') as response:
            return response.json()
    except Exception:
        return error_during_api_access(url)
