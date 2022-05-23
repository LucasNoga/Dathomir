'''main package'''

import logging
import sys

from config import Config, load_config
import core

log = logging.getLogger("dathomir")

PROJECT = "Dathomir"
VERSION = "v1.0.0"


def main():
    '''Program entrypoint'''
    setup_logger()
    config: Config = load_config('config.json')
    setup_log_level(config)

    log.info('Project: %s - %s', PROJECT, VERSION)

    core.start("gitlab")


def setup_logger():
    '''Setup logging format'''
    # Syntax of the log
    log_formatter = '[%(asctime)s] | %(levelname)s : %(message)s'
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    formatter = logging.Formatter(log_formatter, date_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    log.addHandler(stdout_handler)


def setup_log_level(config: Config):
    '''Setup log levelling'''
    debug: int = logging.DEBUG if config.debug else logging.INFO
    log.setLevel(debug)
    log.debug('Set debug mode')


if __name__ == '__main__':
    main()
