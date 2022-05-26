'''help to manage path'''
import logging

from pathlib import Path

log = logging.getLogger('dathomir')


def get_app_path(filepath: Path) -> Path:
    '''Get path of application'''
    return Path(filepath).parent.absolute()


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

    project_folder = Path(project_folder).parent
    basename: str = Path(path).stem
    repository_folder = Path(dns, project_folder, basename)

    folder_to_create: str = Path(base_folder, repository_folder)
    log.debug("Folder to create %s", folder_to_create)
    return folder_to_create
