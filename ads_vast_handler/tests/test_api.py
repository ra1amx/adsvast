from ads_vast_handler.ad_controller import *

test_token = "88ad3b5e-c2b5-4cde-b696-c20145b559b6"

async def test_creatives_fetching():
    creatives = await CreativeStorageHelper().fetch_creatives_or_init(test_token)
    assert creatives

async def test_get_ad_list(aiohttp_client, loop):
    client = await aiohttp_client(init_server({}))
    response = await client.get(f"/api/ad_list?token={test_token}")

    assert response.status == 200
    response_data = await response.text()
    print(response_data)