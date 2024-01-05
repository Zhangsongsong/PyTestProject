import os
from pathlib import Path

dir_name = '/picture'

folder_path = Path(os.getcwd() + dir_name)


def change_file_name():
    for file_path in folder_path.iterdir():
        name = file_path.name
        if name.find('_orig'):
            new_name = name.replace('_orig', '')
            os.rename(os.path.join(folder_path.absolute(), file_path.name), os.path.join(folder_path.absolute(), new_name))
            print()


change_file_name()
