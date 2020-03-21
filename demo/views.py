from aiohttp import web
from aiohttp_jinja2 import template


@template('index.html')
async def index(request):
    return {'site_name': request.app['config'].get('site_name')}

