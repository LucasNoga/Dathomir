'''Console interface'''

import logging

import inquirer
from prettytable import PrettyTable

import core
from config import Server, constants
from interface import Interface

log = logging.getLogger('dathomir')


class Console(Interface):
    '''Handle console interface'''

    def launch(self):
        log.info('Project: %s - %s', constants.PROJECT, constants.VERSION)
        self.show_servers()
        server = self.select_server()
        log.info("Selected: %s", server)

        # Start backup
        core.start(server, self.config.repository)

    def show_servers(self):
        '''Show servers'''
        table = PrettyTable(['Id', 'Git Server', 'Url', 'Token'])
        for idx, server in enumerate(self.config.servers):
            table.add_row([idx+1, server.type, server.url, server.token])
        print("\n\t\t\t\tServers Git")
        print(table)
        print("\n")

    def select_server(self) -> Server:
        '''Select git server among available'''
        servers = []
        for idx, server in enumerate(self.config.servers):
            index = idx+1
            server_name = f"{index}: {server.url}"
            servers.append((server_name, index,))

        print(servers)
        questions = [inquirer.List(name="servers",
                                   message="Choose your git server",
                                   choices=servers)
                     ]

        choice = inquirer.prompt(questions)['servers']
        srv = self.config.servers[choice-1]
        return srv
