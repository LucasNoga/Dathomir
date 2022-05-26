'''Console interface'''

import logging
import re
import sys

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
        try:
            core.start(server, self.config.repository)
        except KeyboardInterrupt:
            sys.exit(0)

    def show_servers(self):
        '''Show servers'''
        table = PrettyTable(['Id', 'Name', 'Git Server', 'Url', 'Token'])
        for idx, server in enumerate(self.config.servers):
            table.add_row([idx+1, server.name, server.type,
                          server.url, server.token])
        print("\n\t\t\t\tServers Git")
        print(table)
        print("\n")

    def select_server(self) -> Server:
        '''Select git server among available'''
        servers = []
        for idx, server in enumerate(self.config.servers):
            index = idx+1
            server_name = f"{index}: Name: {server.name} - Url: {server.url}"
            servers.append((server_name, index,))

        log.debug("Servers proposed %s", servers)
        questions = [inquirer.List(name="servers",
                                   message="Choose your git server",
                                   choices=servers)
                     ]

        choice = inquirer.prompt(questions)['servers']
        srv = self.config.servers[choice-1]
        return srv

    def configuration(self):
        '''Handle configuration'''
        self.show_servers()
        print("\t\t\t\tConfiguration Mode")
        choices = [("1 - Add a new git server config", 1),
                   ("2 - Remove a new git server config", 2)]
        questions = [inquirer.List(name="choice",
                                   message="What do you want to do ?",
                                   choices=choices)
                     ]

        choice = inquirer.prompt(questions)['choice']
        if choice == 1:
            self.add_server()
        elif choice == 2:
            self.remove_server()

    def add_server(self):
        '''Add a new server'''
        log.debug("Add a new configuration")
        questions = [
            inquirer.List(
                name='git_type',
                message="Type of the server",
                choices=[("Gitlab", 'gitlab'), ('Github', 'github')]
            ),
            inquirer.Text(
                name='url',
                message="Url of your server (ex: https://github.com)",
                validate=lambda _, x: re.match(
                    r"^http[s]?:\/\/(www\.)?(.*)?\/?(.)*", x)
            ),
            inquirer.Text(
                name='token',
                message="Token of your account",
                validate=lambda _, x: len(x) >= 5
            ),
            inquirer.Text(
                name='name',
                message="Name of the server (identify it)",
                validate=lambda _, x: len(x) >= 3
            ),
        ]
        loop_ok: int = 1
        while loop_ok:
            answers = inquirer.prompt(questions)
            print("List of your answers")
            for key, value in answers.items():
                print(f"{key} : {value}")

            confirmations = [
                inquirer.List(
                    name='confirmation',
                    message="Is configuration is ok ?",
                    choices=[("Yes", '1'), ('No', '0')]
                ),
            ]

            answer = inquirer.prompt(confirmations)['confirmation']
            if int(answer) == 1:
                break
            else:
                print("Retry to add server git")

        self.config.add_server(answers)
        print("Your new server is added")

    def remove_server(self):
        '''Remove a server'''
        log.debug("Remove a configuration")
        servers = []
        for idx, server in enumerate(self.config.servers):
            index = idx+1
            server_name = f"{index}: Name: {server.name} - Url: {server.url}"
            servers.append((server_name, index,))

        questions = [
            inquirer.List(
                name="servers",
                message="Choose your git server",
                choices=servers
            )
        ]

        choice = inquirer.prompt(questions)['servers']
        index = choice-1
        server = self.config.servers[index]

        confirmations = [
            inquirer.List(
                name='confirmation',
                message=f"Are you sur to delete : {server.name} - Url: {server.url} ?",
                choices=[("Yes", '1'), ('No', '0')]
            ),
        ]

        answer = inquirer.prompt(confirmations)['confirmation']
        if int(answer) == 1:
            print("Removing server: Name: {server.name} - Url: {server.url}")
            self.config.remove_server(index)
            print("You server has been deleted")
            self.show_servers()
