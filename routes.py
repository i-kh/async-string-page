from request_handler import websocket_handler
from views import index


def setup_routes(app):
    app.router.add_get('/', index),
    app.router.add_get('/ws', websocket_handler)