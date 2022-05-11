import os
import shutil
import platform
import os_tools.tools as f

# тесты для "грязных" функций
def test_create_dir():
    dir_name = 'test_dir_1'
    if os.path.exists(dir_name): os.rmdir(dir_name)
    f.create_dir(dir_name)
    assert os.path.exists(dir_name)
    os.rmdir(dir_name)

def test_del_file_or_dir():
    dir_name = 'test_dir_2'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    f.del_file_or_dir(dir_name)
    assert not os.path.exists(dir_name)
    file_name = 'test_file_del'
    if not os.path.exists(file_name):
        open(file_name, mode='a').close()
    f.del_file_or_dir(file_name)
    assert not os.path.exists(file_name)
