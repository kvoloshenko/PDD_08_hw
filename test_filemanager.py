import os_tools.tools as f
import os
import shutil

# тесты для "чистых" функций
def test_about():
    assert f.about() == '(c) Konstantin Voloshenko'

# тесты для "грязных" функций
def test_info_os():
    assert len(f.info_os()) > 1






