'''Generic module for Git server'''


from abc import abstractmethod


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
    def get_access(self):
        '''Get access to self-hosted GitHub instance
        with private token or personal token authentication'''

    @abstractmethod
    def get_projects(self) -> list:
        '''Get all project with your authentication'''

    @abstractmethod
    def clone_projects(self, projects: list, dest_folder: str):
        '''Get through all git projects to clone it'''

    @abstractmethod
    def clone_project(self, project, dest_folder: str):
        '''Clone the project using os librairy'''
