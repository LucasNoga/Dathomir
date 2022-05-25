'''help to manage path'''
import logging
import os
from pathlib import Path

log = logging.getLogger('dathomir')


def get_root_path(filename: str) -> str:
    '''get path of application'''
    return os.path.realpath(os.path.dirname(filename))


def get_path(base_folder: str = ".", path: str = None) -> tuple[str, Exception]:
    '''Create all folders recursively from path into base_folder'''
    path_without_protocol: str
    try:
        _, path_without_protocol = path.split("@")
    except ValueError:
        return None, Exception(f"No '@' in path {path}")

    project_folder: str = ""
    try:
        dns, project_folder = path_without_protocol.split(":")
    except ValueError:
        return None, Exception(f"No ':' in path {path}")

    project_folder = os.path.dirname(project_folder)
    basename: str = Path(path).stem
    repository_folder = os.path.join(dns, project_folder, basename)

    folder_to_create = os.path.join(base_folder, repository_folder)
    log.debug("Folder to create %s", folder_to_create)
    return folder_to_create
