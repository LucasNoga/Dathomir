'''Handle Repositories for gitlab'''

import logging
from enum import Enum

from .github import GitHub
from .git import Git
from .gitlab import GitLab

log = logging.getLogger("dathomir")


class GitServer(Enum):
    '''Type of Git Server'''
    GITHUB = 'github'
    GITLAB = 'gitlab'

    def __str__(self) -> str:
        return self.value


class GitFactory:
    '''Factory to create Git instance (Gitlab or Github)'''

    @classmethod
    def create(cls, url: str, token: str,  git_type: GitServer) -> Git:
        '''Create instance of Git server'''
        git_type = GitServer(git_type)
        log.info("Launch %s cloner", git_type)
        if git_type == GitServer.GITHUB:
            return GitHub(url, token)
        elif git_type == GitServer.GITLAB:
            return GitLab(url, token)
