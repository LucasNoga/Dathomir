'''core module to handle git clone repo'''
import logging
import os

import config.constants as constants

from core.git import Git
from core.git_factory import GitFactory
from config import Server

log = logging.getLogger("dathomir")


def start(server: Server, folder_dest: str):
    '''Start to clone projects from git remote server'''
    git: Git = GitFactory.create(
        url=server.url,
        token=server.token,
        git_type=server.type)
    log.debug(git)

    # Get access
    git.get_access()

    projects = git.get_projects()
    log.info("%s can be imported", len(projects))

    log.info("Cloning %s the projects", len(projects))
    if not os.path.exists(folder_dest):
        log.info("Creating folder %s", folder_dest)
        os.makedirs(folder_dest)
    git.clone_projects(projects, folder_dest)
    log.info("All %s projects are cloned", len(projects))
