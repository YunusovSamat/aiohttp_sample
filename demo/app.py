import jinja2

import aiohttp_jinja2
import asyncpg

from aiohttp import web
from .routes import setup_routers


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    setup_routers(app)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']
    # app['db'] = await asyncpgsa.create_pool(dsn=config['database_url'])
    app['db'] = await asyncpg.create_pool(config['database_url'])


async def on_shutdown(app):
    await app['db'].close()
