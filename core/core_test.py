'''test core module
To execute: python -m unittest -v core
'''

import unittest
import warnings

import pytest

from .github import GitHub
from .gitlab import GitLab

GITHUB_TOKEN = "MgYCIRm3hUqJrLQ0gcAmamfk5x0lfX34BhXo"
GITLAB_TOKEN = "glpat-qCNL5XWGE4ZvNCYnPjDR"


class TestGitAccess(unittest.TestCase):
    '''
    To execute: python -m unittest -v core.TestGitAccess
    '''

    def setUp(self) -> None:
        self.github: GitHub = GitHub("https://github.com", GITHUB_TOKEN)
        self.gitlab: GitLab = GitLab("https://gitlab.com", GITLAB_TOKEN)
        warnings.simplefilter("ignore")

    def tearDown(self):
        del self.github
        del self.gitlab

    def test_access_github_valid(self):
        '''python -m unittest core.CoreTest.test_access_github_valid'''
        connected: bool = self.github.connect()
        self.assertTrue(connected)

    def test_access_gitlab_valid(self):
        '''python -m unittest core.CoreTest.test_access_gitlab_valid'''
        connected: bool = self.gitlab.connect()
        self.assertTrue(connected)

    def test_access_github_invalid(self):
        '''python -m unittest core.CoreTest.test_access_github_invalid'''
        github: GitHub = GitHub("https://github.com", "Invalid_token")
        connected, err = github.connect()
        self.assertFalse(connected)
        self.assertIsNotNone(err)

    def test_access_gitlab_invalid(self):
        '''python -m unittest core.CoreTest.test_access_gitlab_invalid'''
        gitlab: GitLab = GitLab("https://gitlab.com", "Invalid_token")
        connected, err = gitlab.connect()
        self.assertFalse(connected)
        self.assertIsNotNone(err)


class TestGitListProjects(unittest.TestCase):
    '''
    To execute: python -m unittest -v core.TestGitListProjects
    '''

    def setUp(self) -> None:
        self.github: GitHub = GitHub("https://github.com", GITHUB_TOKEN)
        self.gitlab: GitLab = GitLab("https://gitlab.com", GITLAB_TOKEN)
        warnings.simplefilter("ignore")

    def test_access_github_projects(self):
        '''python -m unittest core.TestGitListProjects.test_access_github_projects'''
        self.github.connect()
        projects: list = self.github.get_projects()
        self.assertIsNotNone(projects)

    def test_access_gitlab_projects(self):
        '''python -m unittest core.TestGitListProjects.test_access_gitlab_projects'''
        self.gitlab.connect()
        projects: list = self.gitlab.get_projects()
        self.assertIsNotNone(projects)


class TestGitCloneProject(unittest.TestCase):
    '''
    To execute: python -m unittest -v core.TestGitAccess
    '''

    def setUp(self) -> None:
        self.github: GitHub = GitHub("https://github.com", GITHUB_TOKEN)
        self.gitlab: GitLab = GitLab("https://gitlab.com", GITLAB_TOKEN)
        self.folder = 'repositories_test'
        warnings.simplefilter("ignore")

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_clone_github_project(self):
        '''python -m unittest core.TestGitCloneProject.test_clone_github_project'''
        self.github.connect()
        project: list = self.github.get_projects()[0]
        self.github.clone_project(project, self.folder)

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_clone_gitlab_project(self):
        '''python -m unittest core.TestGitCloneProject.test_clone_gitlab_project'''
        self.gitlab.connect()
        project: list = self.gitlab.get_projects()[0]
        self.gitlab.clone_project(project, self.folder)


if __name__ == '__main__':
    unittest.main()
