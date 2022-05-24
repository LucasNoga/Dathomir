'''Handle Repositories for gitlab'''

import logging
import os

from git import Repo
from git.exc import GitCommandError
from gitlab import Gitlab
from gitlab.exceptions import GitlabAuthenticationError
from gitlab.v4.objects import Project

from .git import Git

log = logging.getLogger("dathomir")


class GitLab(Git):
    '''Gitlab instance to handle project'''

    remote: Gitlab

    def get_access(self) -> Gitlab:
        '''Get access to self-hosted GitLab instance
        with private token or personal token authentication'''
        self.remote = Gitlab(url=self.url, private_token=self.token)
        try:
            self.remote.auth()
            log.info("Access valid to %s", self.url)
        except GitlabAuthenticationError:
            log.critical("Can't access to '%s' with your token", self.url)

    def get_projects(self) -> list:
        '''Get all project with your authentication'''
        return self.remote.projects.list(all=True)

    def clone_projects(self, projects: list, dest_folder: str):
        '''Get through all git projects to clone into dest folder'''
        log.info("Clonning projects into %s", dest_folder)
        for project in projects:
            self.clone_project(project, dest_folder)

    def clone_project(self, project: Project, dest_folder: str):
        '''Clone the project into dest folder'''
        log.debug("Get %s - id=%d - url=%s",
                  project.name, project.id, project.ssh_url_to_repo)
        repo_folder = os.path.join(dest_folder, project.name)
        log.info("Cloning into project %s", repo_folder)
        try:
            Repo.clone_from(project.ssh_url_to_repo, repo_folder)
            log.info("%s cloned", repo_folder)
        except GitCommandError:
            log.info("Repo already exists updating it")
            repo = Repo(repo_folder)
            if not repo.bare:
                log.debug('Repo at %s successfully loaded.', repo_folder)
                repo.remotes.origin.pull()
                log.info("Repo %s updated", repo_folder)
            else:
                log.debug('Could not load repository at %s', repo_folder)

    def __str__(self):
        return f"GitLab instance of {self.dns}"
