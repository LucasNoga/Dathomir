'''Generic interface'''

from abc import abstractmethod
from config import Config


class Interface:
    '''Interface to handle several type of interfaces'''

    config: Config

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def launch(self):
        '''Launch application in console or gui'''

    @abstractmethod
    def show_servers(self):
        '''Show servers available'''

    @abstractmethod
    def select_server(self):
        """Select a server"""
