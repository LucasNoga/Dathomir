'''core module to handle git clone repo'''
import logging
import os
import sys

from gitlab import GitlabAuthenticationError
from github.GithubException import BadCredentialsException

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

    # Get access
    try:
        git.get_access()
        log.info("Access valid to %s", git.url)

        projects = git.get_projects()
        log.info("%s can be imported", len(projects))

        log.info("Cloning %s the projects", len(projects))

        if not os.path.exists(folder_dest):
            log.info("Creating folder %s", folder_dest)
            os.makedirs(folder_dest)

        git.clone_projects(projects, folder_dest)
        log.info("All %s projects are cloned", len(projects))

    # GitLab Exception token invalid
    except GitlabAuthenticationError as exp:
        log.critical("Status Code: %s"
                     "\nMessage: %s"
                     "\nCan't access to '%s' with your token '%s'."
                     "\nPlease set a valid token to get access to to '%s' repositories",
                     exp.response_code, exp.error_message, git.url, git.token, git.url)
        log.info("Exiting...")
        sys.exit(1)

    # GitHub Exception token invalid
    except BadCredentialsException as exp:
        log.critical("Status Code: %s"
                     "\nMessage: %s"
                     "\nCan't access to '%s' with your token '%s'."
                     "\nPlease set a valid token to get access to to '%s' repositories",
                     exp.status, exp.data['message'], git.url, git.token, git.url)
        log.info("Exiting...")
        sys.exit(1)
