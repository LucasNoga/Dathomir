'''Handle system methods'''

import logging
import platform

log = logging.getLogger('dathomir')


def detect_os() -> str:
    '''detect os which launch app'''
    log.debug("OS: %s, Version: %s", platform.system(), platform.release())
    return platform.system()
