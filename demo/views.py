from aiohttp import web
from aiohttp_jinja2 import template


@template('index.html')
async def index(request):
    return {'site_name': request.app['config'].get('site_name')}


async def post(request):
    async with request.app['db'].acquire() as con:
        result = await con.fetch('SELECT * FROM tmp;')

    return web.Response(body=str(result[0]['id']))

