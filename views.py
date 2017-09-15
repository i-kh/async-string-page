import aiohttp_jinja2

from constants import STRING_LENGTH
from utils import get_random_str


@aiohttp_jinja2.template('index.html')
async def index(self):
    return {'string': get_random_str(STRING_LENGTH)}