import base64

import jinja2

import aiohttp_jinja2
import asyncpg
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from aiohttp import web
from .routes import setup_routers


# @web.middleware
# async def user_session_middleware(request, handler):
#     request.session = await get_session(request)
#     response = await handler(request)
#     return response


# def setup_middlewares(app):
#     app.middlewares.append(user_session_middleware)


async def create_app(config: dict):
    app = web.Application(debug=True)

    secret_key = base64.urlsafe_b64decode(config['secret_key'].encode())
    setup(app, EncryptedCookieStorage(secret_key))

    setup_routers(app)
    # setup_middlewares(app)

    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )

    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)

    return app


async def on_start(app):
    config = app['config']
    app['db'] = await asyncpg.create_pool(config['database_url'])


async def on_shutdown(app):
    await app['db'].close()
