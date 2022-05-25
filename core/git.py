'''Generic module for Git server'''

import logging
from abc import abstractmethod

log = logging.getLogger("dathomir")


class Git:
    '''Gitlab instance to handle project'''
    url: str  # Url of Gitlab repository
    dns: str  # Only dns and not all URI
    token: str  # Authentication token
    type: str  # Type GitLab or GitHub

    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self.dns = self.url.split("//")[-1]  # Escape https://
        self.token = token

    @abstractmethod
    def connect(self) -> tuple[str, Exception]:
        '''Get access to Git Server account (Github.com, Gitlab.com)
        or self-host instance with private token or personal token authentication
        '''

    @abstractmethod
    def get_projects(self) -> list:
        '''Get all project with your authentication'''

    def clone_projects(self, projects: list, dest_folder: str):
        '''Get through all git projects to clone into dest folder'''
        log.info("Clonning projects into %s", dest_folder)
        projects = sorted(projects, key=lambda k: k.id)
        for idx, project in enumerate(projects):
            log.info("(%s/%s) Cloning '%s' project...",
                     idx+1, len(projects), project.name)
            self.clone_project(project, dest_folder)

    @abstractmethod
    def clone_project(self, project, dest_folder: str):
        '''Clone the project into dest folder using git clone'''

    @abstractmethod
    def update_project(self, repo_path: str):
        '''Update repo project using git pull'''
