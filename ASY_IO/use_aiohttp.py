# aiohttp是基于asyncio实现的HTTP框架

# 使用aiohttp编写一个服务器，来处理下面连个URL:
# /:首页，返回b'<h1>Index</h1>'
# /hello/{name}：根据URL参数返回文本hello, %s!
# 运行之后，在浏览器中输入http://localhost:8000/hello/Degel

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

