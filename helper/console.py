'''Utilities module'''

import logging
import getopt
import sys

log = logging.getLogger('dathomir')

SHORT_OPTIONS = 'dc'
LONG_OPTIONS = ['debug', 'console']


def get_options() -> tuple[list[tuple[str, str]], list[str]]:
    '''Get all options from console'''
    return getopt.getopt(
        sys.argv[1:], SHORT_OPTIONS, LONG_OPTIONS)


def is_debug() -> bool:
    '''Check if we launch into debug mode'''
    options: list = ["-d", "--debug"]  # Options to check
    try:
        arguments, _ = get_options()

        for current_argument, _ in arguments:
            if current_argument in (options):
                log.info("Option debug found")
                return True
    except getopt.error:
        pass
    return False


def is_console() -> bool:
    '''Check if we launch into console mode'''
    options: list = ["-c", "--console"]  # Options to check
    try:
        arguments, _ = get_options()

        for current_argument, _ in arguments:
            if current_argument in (options):
                log.debug("Option console found")
                return True
    except getopt.error:
        pass
    return False
