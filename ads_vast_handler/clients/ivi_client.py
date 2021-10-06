import yaml
import aiohttp

from ads_vast_handler.clients.singleton import *
from vast_parser.vast_parser import vast2

_config_filepath: str = "ivi_conf"

class IviClient(metaclass=Singleton):

    def __init__(self):
        self._parse_config()

    def _parse_config(self):
        with open(f"config/{_config_filepath}.yml", "r") as config:
            config_data = yaml.load(config)

            self._ivi_url = config_data["url"]
            self._ivi_app_version = config_data["app_version"]
            self.ivi_default_creatives_fetch = f"{self._ivi_url}/?app_version={self._ivi_app_version}"

    async def request_creatives(self, ivi_uri="") -> vast2.VAST:
        ivi_uri = ivi_uri if ivi_uri != "" else self.ivi_default_creatives_fetch

        async with aiohttp.ClientSession() as session:
            ivi_creatives_url = ivi_uri

            async with session.get(ivi_creatives_url) as response:
                ivi_response = await response.text()
                ivi_vast_creatives_data = vast2.VAST.parse(ivi_response)
                return ivi_vast_creatives_data
