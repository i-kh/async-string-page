import aiohttp
from aiohttp import web

from constants import STRING_LENGTH
from utils import get_random_str


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'stop':
                await ws.close()
            else:
                await ws.send_str(get_random_str(STRING_LENGTH))
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws