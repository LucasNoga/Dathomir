'''Handle Repositories for gitlab'''

import logging

from .git import Git

log = logging.getLogger("dathomir")


class GitHub(Git):
    '''Gitlab instance to handle project'''

    # TODO
    def get_access(self):
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
