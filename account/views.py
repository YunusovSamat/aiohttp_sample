from aiohttp import web
from aiohttp_jinja2 import template
from aiohttp_session import get_session

from . import modules


class Index(web.View):
    @template('index.html')
    async def get(self):
        session = await get_session(self)
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

        if not all([data.get(k) for k in ['email', 'password']]):
            return web.HTTPFound(self.url)

        user = await modules.get_user_data(self.app['db'], data['email'])
        if not user:
            return web.HTTPFound(self.url)

        if modules.check_password(user['password'], data['password']):
            session = await get_session(self)
            session['user'] = user['email']
            return web.HTTPFound(self.app.router['index'].url_for())
        else:
            return web.HTTPFound(self.url)

    async def patch(self):
        data = dict(await self.patch())

        if not all([data.get(k) for k in ['old_passw', 'new_passw']]):
            return web.HTTPFound(self.app.router['index'].url_for())

        session = await get_session(self)
        user = await modules.get_user_data(self.app['db'], session['user'])

        if modules.check_password(user['password'], data['old_passw']):
            await modules.change_password(self.app['db'],
                                          data['email'], data['new_passw'])
            return web.HTTPFound(self.app.router['index'].url_for())
        else:
            return web.HTTPFound(self.app.router['index'].url_for())

    async def delete(self):
        session = await get_session(self)
        if session.get('user'):
            await modules.delete_user(self.app['db'], session['user'])
            del session['user']
        return web.HTTPFound(self.app.router['index'].url_for())


class Signup(web.View):
    @template('signup.html')
    async def get(self):
        return dict()

    async def post(self):
        data = dict(await self.post())

        if not all([data.get(k) for k in ['email', 'name', 'surname', 'password']]):
            return web.HTTPFound(self.url)

        user = await modules.get_user_data(self.app['db'], data['email'])
        if user:
            return web.HTTPFound(self.url)

        await modules.insert_new_user(
            self.app['db'], data['email'], data['name'],
            data['surname'], data['password']
        )
        return web.HTTPFound(self.app.router['index'].url_for())


class Logout(web.View):
    async def get(self):
        session = await get_session(self)
        if session.get('user'):
            del session['user']

        return web.HTTPFound(self.app.router['index'].url_for())
