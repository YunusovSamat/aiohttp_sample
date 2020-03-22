from aiohttp import web
from aiohttp_jinja2 import template
from aiohttp_session import get_session

from . import modules


class UserFiles(web.View):
    @template('user_files.html')
    async def get(self):
        session = await get_session(self)
        if not session.get('user'):
            return web.HTTPFound(self.app.router['login'].url_for())

        files = await modules.get_files(self.app['db'], session['user'])
        context = {'files': files}
        return context

    async def post(self):
        session = await get_session(self)
        if not session.get('user'):
            return web.HTTPFound(self.app.router['login'].url_for())

        data = dict(await self.post())
        if not all([data.get(k) for k in ['file', 'url']]):
            return web.HTTPFound(self.url)

        await modules.insert_file(self.app['db'], session['user'],
                                  data['file'], data['url'])

        return web.HTTPFound(self.app.router['user_files'].url_for())
