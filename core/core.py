'''core module to handle git clone repo'''
import logging
import sys
from pathlib import Path

from config import Server

from .git import Git
from .git_factory import GitFactory

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

    folder: Path = Path(folder_dest)
    if not folder.exists():
        log.info("Creating folder %s", folder)
        folder.mkdir()

    git.clone_projects(projects, folder_dest)
    log.info("All %s projects are cloned", len(projects))
