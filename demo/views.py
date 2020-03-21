import hashlib

from aiohttp import web
from aiohttp_jinja2 import template
from aiohttp_session import get_session

from . import query


@template('index.html')
async def index(request):
    session = await get_session(request)
    context = dict()
    if session.get('user'):
        context['user'] = session.get('user')
    return context


class Login(web.View):
    @template('login.html')
    async def get(self):
        return dict()

    async def post(self):
        data = dict(await self.post())
        async with self.app['db'].acquire() as con:
            user = await con.fetchrow(query.SLT_USER, data['email'])
        if not user:
            location = self.app.router['login'].url_for()
            return web.HTTPFound(location=location)

        if user['password'] == hashlib.sha256(data['password'].encode('utf8')).hexdigest():
            session = await get_session(self)
            session['user'] = user['email']
            location = self.app.router['index'].url_for()
            return web.HTTPFound(location=location)
        else:
            location = self.app.router['login'].url_for()
            return web.HTTPFound(location=location)


class Signup(web.View):
    @template('signup.html')
    async def get(self):
        return dict()

    async def post(self):
        data = dict(await self.post())
        async with self.app['db'].acquire() as con:
            user = await con.fetchrow(query.SLT_USER,
                                            data['email'])
            if user:
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


class Logout(web.View):
    async def get(self):
        session = await get_session(self)
        del session['user']

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)
