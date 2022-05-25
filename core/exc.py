'''Exception core module'''


class AuthGitException(Exception):
    '''Excpetion when the connect method for github or gitlab failed'''

    def __init__(self, status_code: str, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Status Code: {self.status_code} - Message: {self.message}"
