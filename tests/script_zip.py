import os
import zipfile
from property import RESOURCES_PATH


def test_add_zip():
    zip_name = 'test_zip.zip'
    with zipfile.ZipFile(zip_name, "w") as zip_file:
        for file_name in os.listdir(RESOURCES_PATH):
            file_path = os.path.join(RESOURCES_PATH, file_name)
            zip_file.write(file_path, file_name)

    with zipfile.ZipFile(zip_name, "r") as zip_file:
        for file_name in os.listdir(RESOURCES_PATH):
            assert file_name in zip_file.namelist()

    # os.remove(zip_name)