'''Config of Git server'''


class Server:
    '''Server on Git'''
    type: str
    url: str
    token: str

    def __init__(self, git_type: str, url: str, token: str):
        self.type = git_type
        self.url = url
        self.token = token

    def __str__(self):
        return f"Git server - {self.type} - url: {self.url} - token: {self.token}"
