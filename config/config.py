'''Config of Dathomir'''

import json
import logging
import os

import helper

from config.server import Server

log = logging.getLogger('dathomir')


class Config:
    '''Config of the application'''
    path: str
    debug: str = 'true'
    repository: str
    servers: list[Server]

    def add_server(self, data):
        '''Add server new server in list with data'''
        log.debug("Add server with data %s", data)
        [git_type, url, token, name] = data.values()
        server: Server = Server(
            url=url,
            token=token,
            git_type=git_type,
            name=name
        )
        self.servers.append(server)
        log.debug("Server %s added", server)
        self.save_config()

    def remove_server(self, index):
        '''Delete server among servers list from config'''
        log.debug("Delete server with index %s", index)
        server: Server = self.servers[index]
        del self.servers[index]
        log.debug("Name: %s deleted", server.name)
        self.save_config()

    def save_config(self):
        '''Save config into the path define'''
        log.debug("Saving config %s", self.path)
        config = {
            'repository': os.path.basename(self.repository),
            'servers': [{"name": server.name,
                         "type": server.type,
                         "url": server.url,
                         "token": server.token}
                        for server
                        in self.servers
                        ]
        }
        # log.debug("New config %s", json.dumps(config, indent=2))
        with open(self.path, 'w', encoding="utf-8") as document:
            json.dump(config, document, indent=2)


def load_config(filepath: str) -> Config:
    '''Create config object loading data from config.json file'''
    config: Config = Config()
    try:
        with open(filepath, mode='r', encoding='utf-8') as document:
            json_data = json.load(document)

            config.path = filepath
            config.debug = json_data.get('debug', 'true')

            backup_folder = json_data.get('repository', 'repositories')
            config.repository = f"{helper.get_root_path(filepath)}/{backup_folder}"

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
