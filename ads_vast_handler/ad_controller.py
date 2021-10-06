from ads_vast_handler.creative_storage_helper import CreativeStorageHelper
import asyncio

import aiohttp
from aiohttp import web

from ads_vast_handler.clients import ivi_client
from vast_parser.vast_parser import vast2

routes = web.RouteTableDef()

@routes.get("/api/ad_list")
async def get_ad_list(request: web.Request) -> web.Response:
    request_data: dict = request.query
    
    if "token" not in request_data:
        return web.json_response(status=401)
    partner_token: str = request_data["token"] # Log
    
    creatives = await CreativeStorageHelper().fetch_creatives_or_init(partner_token)
    return web.json_response(creatives)


@routes.get("/api/ad")
async def get_ad(request: web.Request) -> web.Response:
    ...

def init_server(argv):
    app = web.Application()
    app.add_routes(routes)
    return app