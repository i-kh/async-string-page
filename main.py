import os

import aiohttp_jinja2
import jinja2
from aiohttp import web
from middlewares import setup_middlewares
from routes import setup_routes

app = web.Application()
setup_routes(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

setup_middlewares(app)
app.router.add_static('/static/',
                      path=os.path.join(os.getcwd(), 'static'),
                      name='static')
web.run_app(app, host='0.0.0.0', port=8080)
