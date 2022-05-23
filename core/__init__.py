'''core module to handle git clone repo'''
import logging
import os

import config.constants as constants

from core.git import Git
from core.git_factory import GitFactory

log = logging.getLogger("dathomir")


def start(git_type: str):
    '''Start to clone projects from git remote server'''
    git: Git = GitFactory.create(
        url=constants.GIT_REMOTE_URL,
        token=constants.GIT_REMOTE_TOKEN,
        git_type=constants.GIT_REMOTE_TYPE)
    log.debug(git)

    projects = git.get_projects()
    log.info("%s can be imported", len(projects))

    log.info("Cloning %s the projects", len(projects))
    if not os.path.exists(constants.REPO_FOLDER):
        log.info("Creating folder %s", constants.REPO_FOLDER)
        os.makedirs(constants.REPO_FOLDER)
    git.clone_projects(projects, constants.REPO_FOLDER)
    log.info("All %s projects are cloned", len(projects))
