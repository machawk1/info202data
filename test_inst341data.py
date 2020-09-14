import os
import shutil
import inst341data

def test_get_data():
    inst341data.get_module_2("inst341")
    assert os.path.isdir("inst341")
    shutil.rmtree("inst341")
    os.remove("inst341.zip")

def test_missing():
    inst341data.get_module_2("foo")
