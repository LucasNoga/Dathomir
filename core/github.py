'''Handle Repositories for gitlab'''

import logging

from .git import Git

log = logging.getLogger("dathomir")


class GitHub(Git):
    '''Gitlab instance to handle project'''
    # Url of Gitlab repository
    url: str
    # Only dns and not all URI
    dns: str
    # Authentication token
    token: str
    type: str = 'github'

    remote: None

    def __init__(self, url: str, token: str):
        super().__init__(url, token)
        self.url = url
        self.dns = self.url.split("//")[-1]  # Escape https://
        self.token = token

        self.access()

    # TODO
    def access(self):
        '''Get access to self-hosted GitHub instance
        with private token or personal token authentication'''

    # TODO
    def get_projects(self) -> list:
        '''Get all project with your authentication'''
        return []

    # TODO
    def clone_projects(self, projects: list, dest_folder: str):
        '''Get through all git projects to clone it'''

    # TODO
    def clone_project(self, project, dest_folder: str):
        '''Clone the project using os librairy'''

    def __str__(self):
        return f"GitHub instance of {self.dns}"
