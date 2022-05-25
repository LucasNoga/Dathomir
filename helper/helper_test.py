'''test helper module'''
import unittest

from .path import get_path


class HelperTest(unittest.TestCase):
    '''
    To execute: python -m unittest -v helper
    To execute one : python -m unittest helper.HelperTest.test_get_path
    '''

    def setUp(self):
        self.base_folder = 'repositories'

    def test_get_path(self):
        '''python -m unittest helper.HelperTest.test_get_path'''
        path: str = "git@gitlab.com:infra/monitoring.git"
        expected: str = "repositories/gitlab.com/infra/monitoring"
        value = get_path(self.base_folder, path)
        self.assertEqual(value, expected)

    def test_get_path_group_depths_1(self):
        '''python -m unittest helper.HelperTest.test_get_path_group_depths_1'''
        path: str = "git@github.com:ethereum/go-ethereum.git"
        expected: str = "repositories/github.com/ethereum/go-ethereum"
        value = get_path(self.base_folder, path)
        self.assertEqual(value, expected)

    def test_get_path_group_depths_2(self):
        '''python -m unittest helper.HelperTest.test_get_path_group_depths_2'''
        path: str = "git@github.com:ethereum/explorer/api.git"
        expected: str = "repositories/github.com/ethereum/explorer/api"
        value = get_path(self.base_folder, path)
        self.assertEqual(value, expected)

    def test_get_path_self_host(self):
        '''python -m unittest helper.HelperTest.test_get_path_self_host'''
        path: str = "git@gitlab.company.com:company-group/company-app.git"
        expected: str = "repositories/gitlab.company.com/company-group/company-app"
        value = get_path(self.base_folder, path)
        self.assertEqual(value, expected)

    def test_get_path_with_no_arobase(self):
        '''python -m unittest helper.HelperTest.test_get_path_with_no_arobase'''
        path: str = "git.github.com:ethereum/go-ethereum.git"
        value, exc = get_path(self.base_folder, path)
        self.assertIsNone(value)
        self.assertIsNotNone(exc)

    def test_get_path_with_no_colon(self):
        '''python -m unittest helper.HelperTest.test_get_path_with_no_colon'''
        path: str = "git@github.com/ethereum/go-ethereum.git"
        value, exc = get_path(self.base_folder, path)
        self.assertIsNone(value)
        self.assertIsNotNone(exc)


if __name__ == '__main__':
    unittest.main()
