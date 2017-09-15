import aiohttp_jinja2
from aiohttp import web


def setup_middlewares(app):
    error_middleware = error_pages({404: handle_404,
                                    500: handle_500})
    app.middlewares.append(error_middleware)


def error_pages(overrides):
    async def middleware(app, handler):
        async def middleware_handler(request):
            try:
                response = await handler(request)
                override = overrides.get(response.status)
                if override is None:
                    return response
                else:
                    return await override(request, response, app)
            except web.HTTPException as ex:
                override = overrides.get(ex.status)
                if override is None:
                    raise
                else:
                    return await override(request, ex, app)

        return middleware_handler

    return middleware


async def handle_404(request, response, app):
    response = aiohttp_jinja2.render_template(
        aiohttp_jinja2.get_env(app).get_template('404.html'), request, {})
    return response


async def handle_500(request, response, app):
    response = aiohttp_jinja2.render_template(
        '500.html', request, {})
    return response
