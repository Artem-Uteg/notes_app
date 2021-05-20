from aiohttp import web
import storage
import json

async def index(_req):
    return web.Response(status=302, headers={"Location": "/index.html"})


temp_history = []
async def plus_one(req):
    #[[1, text]
    try: body = await req.json()
    except: return web.Response(text='not_json', status=500)

    if "action" not in body: return web.Response(text='no_action', status=500)
    
    if body["action"] == 'history':
        count = body["arg"][0]
        id = body["arg"][1]
        #storage.take_info(req.app)
        return web.Response(text=json.dumps(await storage.take_info(req.app['storage'], count, id)))
        #return web.Response(text=json.dumps(await storage.take_info(req.app['storage']))) #переделать и выдавать 5 первых сообщений
    
    if body["action"] == '+1':
        if not isinstance(body["arg"], str) or len(body["arg"]) > 255:#нет сообщения: выдать ошибка
            return web.Response(text='error', status=418)

        try: id = await storage.store(req.app['storage'], body["arg"]) #temp_history.append(["01.01.1977", body["arg"], len(temp_history)])
        except Exception as err: print("Failed to store", body["arg"], "--", err); return web.Response(text='error', status=500)
        #добавить сообщение в историю

        return web.Response(text=str(id))
'''
     if body["action"] == 'next':
         if type(body["arg"]) == int:
             return  web.Response(text=json.dumps(temp_history)[len(temp_history)-body["arg"]:len(temp_history)-body["arg"]+5])
        #return web.Response(text=json.dumps(await storage.take_info_another(req.app['storage']))) #переделать и выдавать 5 первых сообщений
        

    return web.Response('not_supported', status=500)
'''

"""
    if "arg" not in body: return web.Response(text='no_arg', status=500)

    try: number = str(body["arg"]) #isinstance(n, str)                                                                                      json.dumps({"date": [], "text": []})                         [ [],[] ] // [], [] [[date, text, id],[...]]
    except: return web.Response(text='bad_arg', status=500)

    try: await storage.store(req.app['storage'], number)
    except Exception as err: print("Failed to store", number, "--", err)

    #if number % 10 == 0: return web.Response(text='bad_numb', status=418)
    return web.Response(text=json.dumps({
        "answer": puk.json)          #str(number + 1)
    }))
"""

async def init_storage(app):
    app['storage'] = await storage.init()

async def free_storage(app):
    await storage.free(app['storage'])

def main():
    app = web.Application()

    app.on_startup.append(init_storage)
    app.on_cleanup.append(free_storage)
    
    app.add_routes([
        web.get('/', index),
        web.static('/', 'client'),
        web.post('/', plus_one),
    ])

    web.run_app(app, host='127.0.0.1', port='9118')

main()

