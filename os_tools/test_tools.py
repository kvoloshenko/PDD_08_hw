import os
import shutil
import platform
import os_tools.tools as f


def test_create_dir():
    dir_name = 'test_dir_1'
    if os.path.exists(dir_name): os.rmdir(dir_name)
    f.create_dir(dir_name)
    assert os.path.exists(dir_name)
    os.rmdir(dir_name)
