import os
import shutil
import pytest


CURRENT_FILE_PATH = os.path.abspath(__file__)
ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
RESOURCES_PATH = os.path.join(ROOT_PATH, 'resources', )