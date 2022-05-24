'''help to manage path'''
import logging
import os
from pathlib import Path
log = logging.getLogger('dathomir')


def get_path(base_folder: str = ".", path: str = None):
    '''Create all folders recursively from path into base_folder'''
    dns: str = path.split("@")[1].split(":")[0]
    project_folder: str = os.path.dirname(path.split(":")[1])
    basename: str = Path(path).stem

    folder_to_create = os.path.join(base_folder, dns, project_folder, basename)

    log.debug("Folder to create %s", folder_to_create)
    os.makedirs(folder_to_create, exist_ok=True)
    return folder_to_create
