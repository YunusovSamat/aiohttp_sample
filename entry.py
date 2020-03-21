from aiohttp import web

import aioreloader

from demo.app import create_app
from demo.settings import load_config

app = create_app(config=load_config())
aioreloader.start()

if __name__ == '__main__':
    web.run_app(app, )

