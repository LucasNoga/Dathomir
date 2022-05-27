'''Gui interface'''

import logging

from interface import Interface

log = logging.getLogger('dathomir')


class Gui(Interface):
    '''Handle gui interface'''

    def launch(self):
        '''Launch application in console or gui'''
        log.info("Start GUI")

    def show_servers(self):
        '''Show servers available'''
        pass

    def select_server(self):
        '''Select a server'''
        pass

    def add_server(self):
        '''Add a new server'''
        pass

    def remove_server(self):
        '''Remove a server'''
        pass
