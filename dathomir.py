'''main package'''

import logging
import sys
from pathlib import Path

import helper
from config import Config, load_config
from config.constants import CONFIG_PATH
from interface import Console, Gui, Interface

log = logging.getLogger("dathomir")


def main():
    '''Program entrypoint'''
    # Logger
    setup_logger()
    app_path: Path = helper.get_app_path(__file__)
    set_log_level()
    log.debug("Application path: %s", app_path)

    # Config
    config_path: Path = Path(app_path, CONFIG_PATH)
    config: Config = load_config(config_path)
    if config is None:
        log.critical("No config file found in '%s'", config_path)
        log.info("Exiting...")
        sys.exit(1)

    # Interface (Console or GUI)
    interface: Interface
    if helper.is_console():
        log.info("Launch console mode")
        interface = Console(config)
    else:
        interface = Gui(config)

    # Launch App
    if helper.is_config():
        log.info("Launch config mode")
        Console(config).configuration()
        sys.exit(0)
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
