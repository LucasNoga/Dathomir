'''Config of Dathomir'''

import json
import logging

import helper

from config.server import Server

log = logging.getLogger('dathomir')


class Config:
    '''Config of the application'''
    debug: str = 'true'
    repository: str
    servers: list[Server]


def load_config(filepath: str) -> Config:
    '''Create config object loading data from config.json file'''
    config: Config = Config()
    try:
        with open(filepath, mode='r', encoding='utf-8') as document:
            json_data = json.load(document)
            config.debug = json_data.get('debug', 'true')
            config.repository = f"{helper.get_root_path(filepath)}/{json_data.get('repository', 'repositories')}"
            servers = json_data.get('servers', [])
            config.servers = [
                Server(server['name'], server['type'],
                       server['url'], server['token'])
                for server
                in servers
            ]
    except FileNotFoundError:
        return None
    return config
