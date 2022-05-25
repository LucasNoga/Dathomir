'''main package'''

import os
import logging
import sys

import helper
from config import Config, load_config
from interface import Interface, Console, Gui

log = logging.getLogger("dathomir")


def main():
    '''Program entrypoint'''
    # Logger
    setup_logger()
    app_path = helper.get_root_path(__file__)
    set_log_level()
    log.debug("Application path: %s", app_path)

    # Config
    config_path = os.path.join(app_path, 'config.json')
    config: Config = load_config(os.path.join(
        app_path, 'config.json'))
    if config is None:
        log.critical("No config file found in '%s'", config_path)
        log.info("Exiting...")
        sys.exit(1)

    # Interface (Console or GUI)
    interface: Interface
    if helper.is_console():
        log.info("Launch Console mode")
        interface = Console(config)
    else:
        interface = Gui(config)

    # Launch App
    interface.launch()


def setup_logger():
    '''Setup logging format'''
    # Syntax of the log
    log_formatter = '[%(asctime)s] | %(levelname)s : %(message)s'
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    formatter = logging.Formatter(log_formatter, date_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    log.addHandler(stdout_handler)


def set_log_level():
    '''Set level log'''
    level: int = logging.DEBUG if helper.is_debug() else logging.INFO
    log.setLevel(level)
    log.debug('Set debug mode')


if __name__ == '__main__':
    main()
