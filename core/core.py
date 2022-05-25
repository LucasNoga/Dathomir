'''core module to handle git clone repo'''
import logging
import os
import sys

from config import Server

from core.git import Git
from core.git_factory import GitFactory


log = logging.getLogger("dathomir")


def start(server: Server, folder_dest: str):
    '''Start to clone projects from git remote server'''
    git: Git = GitFactory.create(
        url=server.url,
        token=server.token,
        git_type=server.type)
    log.debug(git)

    _, err = git.connect()
    if err is not None:
        log.error("Can't access to '%s' with your token '%s'.\n"
                  "Please set a valid token to get access to '%s' repositories.",
                  git.url, git.token, git.url)
        log.info("Exiting...")
        sys.exit(1)

    log.info("Access valid to %s", git.url)
    projects = git.get_projects()
    log.info("%s can be imported", len(projects))

    log.info("Cloning %s the projects", len(projects))

    if not os.path.exists(folder_dest):
        log.info("Creating folder %s", folder_dest)
        os.makedirs(folder_dest)

    git.clone_projects(projects, folder_dest)
    log.info("All %s projects are cloned", len(projects))
