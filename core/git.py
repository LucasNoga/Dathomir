'''Generic module for Git server'''


class Git:
    '''Gitlab instance to handle project'''
    # Url of Gitlab repository
    url: str
    # Only dns and not all URI
    dns: str
    # Authentication token
    token: str
    type: str

    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self.dns = self.url.split("//")[-1]  # Escape https://
        self.token = token

    def access(self):
        '''Get access to self-hosted GitHub instance
        with private token or personal token authentication'''
        return

    def get_projects(self) -> list:
        '''Get all project with your authentication'''
        return []

    def clone_projects(self, projects: list, dest_folder: str):
        '''Get through all git projects to clone it'''
        return

    def clone_project(self, project, dest_folder: str):
        '''Clone the project using os librairy'''
        return
