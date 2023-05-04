import os
import shutil
import pytest

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJECT_RESOURCE_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')
PROJECT_USER_PATH = os.path.join(PROJECT_ROOT_PATH, 'user')


@pytest.fixture(scope='session', autouse=True)
def clear_tmp_directory():
    if not os.path.exists(PROJECT_USER_PATH):
        os.mkdir(PROJECT_USER_PATH)
    folder_path = PROJECT_USER_PATH
    for file_object in os.listdir(folder_path):
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
            os.unlink(file_object_path)
        else:
            shutil.rmtree(file_object_path)

    yield