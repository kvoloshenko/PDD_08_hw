import os
import shutil
import platform
import decorators as d
"""
создание папки
"""
def create_dir(dir_name):
    #if not os.path.exists(dir_name): os.mkdir(dir_name)
    os.mkdir(dir_name) if not os.path.exists(dir_name) else print(f'Directory {dir_name} already exist')


"""
удаление файла(папки)
"""
def del_file_or_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(path):
        os.remove(dir_name) if os.path.isfile(dir_name) else os.rmdir(dir_name)
    else:
        print('      Файл или папка отсутсвует')


"""
копировать (файл/папку)
"""
def copy_dir(dir_name, dir_new):
    # print(os.getcwd())
    #dir_name = input('   Введите имя папки или файла: ')
    #dir_new = input('   Введите новое имя папки или файла: ')
    if os.path.exists(dir_name):
        shutil.copy(dir_name, dir_new) if os.path.isfile(dir_name) else shutil.copytree(dir_name, dir_new, False, None)
    else:
        print('      Файл или папка отсутсвует')


def info_dir(type):
    # print(os.listdir())
    items = []
    dir_items = os.listdir()
    if type == 'files': items = [item for item in dir_items if os.path.isfile(item)]
    elif type == 'dirs': items = [item for item in dir_items if not (os.path.isfile(item))]
    elif type == 'all': items = [item for item in dir_items]
    return items

def save_info_dir():
    dir_items = os.listdir()
    l_files = [item for item in dir_items if os.path.isfile(item)]
    l_files.insert(0, 'files')
    l_dirs = [item for item in dir_items if not (os.path.isfile(item))]
    l_dirs.insert(0, 'dirs')
    with open('listdir.txt', 'w') as f:
        len_files = len(l_files)
        #print (f'len_files={len_files}')
        len_dirs = len(l_dirs)
        #print(f'len_dirs={len_dirs}')
        i=len_files
        j=len_dirs
        for file in l_files:
            f.write(f'{file}')
            if i == len_files:
                f.write(': ')
            elif i == 1:
                f.write('\n')
            else: f.write(', ')
            i-=1
        for dir in l_dirs:
            f.write(f'{dir}')
            if j == len_dirs:
                f.write(': ')
            elif j == 1:
                f.write('\n')
            else: f.write(', ')
            j-=1

def info_os():
    #print('      ', platform.platform())
    return platform.platform()

@d.add_separators
def print_f(f):
    print('      ', f())

def about():
    #print('      ', '(c) Konstantin Voloshenko')
    return '(c) Konstantin Voloshenko'
"""
смена рабочей директории
"""
def chenge_dir():
    print(os.getcwd())
    dir_name = input('   Введите новой робочей директории: ')
    if os.path.exists(dir_name):
        os.chdir(dir_name)
        print(os.getcwd())
    else:
        print('      Папка отсутсвует')

if __name__ == '__main__':
    # del_dir()
    # copy_dir()
    # info_dir('dirs')
    # chenge_dir()
    save_info_dir()
