'''Config of Git server'''


class Server:
    '''Server on Git'''
    name: str
    type: str
    url: str
    token: str

    def __init__(self, name: str, git_type: str, url: str, token: str):
        self.name = name
        self.type = git_type
        self.url = url
        self.token = token

    def __str__(self):
        return f"Git server - {self.name} - {self.type} - url: {self.url} - token: {self.token}"
