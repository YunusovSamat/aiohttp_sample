import hashlib

from aiohttp import web
from aiohttp_jinja2 import template

from . import query


@template('index.html')
async def index(request):
    return {'site_name': request.app['config'].get('site_name')}


async def post(request):
    data = {'email': 'sdf', 'name': 'dfa', 'surname': 'dfa', 'password': 'dfa'}
    async with request.app['db'].acquire() as con:
        result = await con.execute('''INSERT INTO users (email, name, surname, password) VALUES (, 'dfda', 'df', 'df')''',
                                   data)

    return web.Response(text='Yes')


class Signup(web.View):
    @template('signup.html')
    async def get(self):
        return dict()

    async def post(self):
        data = await self.post()
        data = dict(data)
        async with self.app['db'].acquire() as con:
            exist_user = await con.fetchrow(query.SLT_EXIST_EMAIL, data['email'])
            if exist_user:
                location = self.app.router['signup'].url_for()
                return web.HTTPFound(location=location)

            if all(data.values()):
                data['password'] = hashlib.sha256(data['password'].encode('utf8')).hexdigest()
                await con.execute(
                    query.INS_USER,
                    data['email'],
                    data['name'],
                    data['surname'],
                    data['password']
                )
        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)
