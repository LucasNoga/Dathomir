'''Handle Repositories for gitlab'''

import logging

from git import Repo
from git.exc import GitCommandError
from github import Github
from github.Repository import Repository

import helper

from .git import Git

log = logging.getLogger("dathomir")


class GitHub(Git):
    '''Gitlab instance to handle project'''
    remote: Github

    def get_access(self):
        '''Get access to self-hosted GitLab instance
        with private token or personal token authentication'''
        self.remote: Github = Github(self.token)

    def get_projects(self) -> list:
        '''Get all project with your authentication'''
        return [project for project in self.remote.get_user().get_repos()]

    def clone_project(self, project: Repository, dest_folder: str):
        '''Clone the project into dest folder using git clone'''

        log.debug("Project info: %s - id=%d - url=%s",
                  project.name, project.id, project.ssh_url)

        repo_path = helper.get_path(dest_folder, project.ssh_url)
        log.info("Cloning into project %s", repo_path)

        try:
            Repo.clone_from(project.ssh_url, repo_path)
            log.info("%s cloned", repo_path)
        except GitCommandError:
            self.update_project(repo_path)

    def update_project(self, repo_path: str):
        '''Update repo project using git pull'''
        log.info("Repo already exists updating it")
        repo = Repo(repo_path)

        if not repo.bare:
            log.debug('Repo at %s successfully loaded.', repo_path)
            try:
                repo.remotes.origin.pull()
                log.info("Repo %s updated", repo_path)
            except GitCommandError:
                log.warning("Repo can't be updated may be it's empty")
        else:
            log.debug('Could not load repository at %s', repo_path)

    def __str__(self):
        return f"GitHub instance of {self.dns}"
