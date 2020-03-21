import jinja2

import aiohttp_jinja2

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
    return app
