import os_tools.tools as f
import os
import shutil



# тесты для "чистых" функций
def test_about():
    assert f.about() == '(c) Konstantin Voloshenko'


# тесты для "грязных" функций




def test_info_dir():
    cur_dir = os.getcwd()
    dir_name = 'test_info_dir'
    os.mkdir(dir_name)
    os.chdir(dir_name)
    os.mkdir('test_dir_1')
    os.mkdir('test_dir_2')
    open('test_file_1', mode='a').close()
    open('test_file_2', mode='a').close()
    assert f.info_dir('dirs') == ['test_dir_1', 'test_dir_2']
    assert f.info_dir('files') == ['test_file_1', 'test_file_2']
    assert f.info_dir('all') == ['test_dir_1', 'test_dir_2', 'test_file_1', 'test_file_2']
    os.chdir(cur_dir)
    # os.rmdir(dir_name)
    shutil.rmtree(dir_name, ignore_errors=True)


def test_info_os():
    assert len(f.info_os()) > 1






