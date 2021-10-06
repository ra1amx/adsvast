import os
import urllib
import uuid

import yaml
from aiohttp import web

from ads_vast_handler.clients import ivi_client
from ads_vast_handler.clients.singleton import *
from vast_parser.vast_parser import vast2

_config_filepath: str = "main_config"

class CreativeStorageHelper(metaclass=Singleton):

    def __init__(self):
        self._parse_config()

        self.creative_storage_cache = {}

    def _parse_config(self):
        with open(f"config/{_config_filepath}.yml", "r") as config:
            config_data = yaml.load(config)

            self.creatives_path = config_data["creatives_path"]
            self.creative_path_uri_prefix = config_data["creative_path_uri_prefix"]

    def _add_new_file_name_to_cache_by_token(self, token: str, new_creative_file_name: str):
        creatives_by_token = set()
                
        if token in self.creative_storage_cache:
            creatives_by_token = set(self.creative_storage_cache[token])

        creatives_by_token.add(new_creative_file_name)
        self.creative_storage_cache[token] = creatives_by_token

    def _download_media_file_by_url(self, media_file_url: str, destination: str) -> str:
        destination_file_name = f"{uuid.uuid4()}.mp4"
        urllib.request.urlretrieve(media_file_url, f"{os.path.abspath(destination)}/{destination_file_name}")

        return destination_file_name

    def _process_vast_document_wrapper(self, vast_document_wrapper: vast2.Wrapper) -> bool:
        return False # Parse later

    def _process_vast_document_inline(self, token: str, vast_document_inline: vast2.InLine) -> bool:
        linears = [creative.linear for creative in vast_document_inline.creatives if creative.linear is not None]

        if not linears:
            return False

        media_files = []
        for linear in linears:
            media_files.extend(linear.mediaFiles)

        # If no media files fetched, try fetching again
        if not media_files:
            return False

        # Download and save media files content
        media_files_fetched = False
        for media_file in media_files:
            media_file_url = media_file.mediaFileUrl
            downloaded_file_name = self._download_media_file_by_url(media_file_url, self.creatives_path)
            
            if downloaded_file_name:
                media_files_fetched = True

                # Cache media files name
                self._add_new_file_name_to_cache_by_token(token, downloaded_file_name)

        return media_files_fetched


    async def _init_creatives(self, token: str) -> bool:
        creatives_initialized = False

        while not creatives_initialized: # Ad timeout or counter
            client = ivi_client.IviClient()
            request_uri = client.ivi_default_creatives_fetch + "&partner_uid=" + token
            print(request_uri)
            vast_document: vast2.VAST = await client.request_creatives(request_uri)

            if vast_document.ad.wrapper is not None:
                creatives_initialized = self._process_vast_document_wrapper(vast_document.ad.wrapper)
            elif vast_document.ad.inLine is not None:
                creatives_initialized = self._process_vast_document_inline(token, vast_document.ad.inLine)

        return creatives_initialized

    def _process_creatives_before_return(self, creatives: list) -> list:
        return [f"{self.creative_path_uri_prefix}/{file_name}" for file_name in creatives]

    async def fetch_creatives_or_init(self, token: str) -> list:

        # Check creatives cache
        if token in self.creative_storage_cache:
            return self._process_creatives_before_return(list(self.creative_storage_cache[token]))

        # Fetch creatives from file system, if no creatives found - initialize
        creatives_list = os.listdir(os.path.abspath(self.creatives_path))
        if creatives_list:
            return self._process_creatives_before_return(creatives_list)
        else:
            await self._init_creatives(token)
            return await self.fetch_creatives_or_init(token)