import os
import shutil
import info202data

def test_get_data():
    info202data.get_module_2("info202")
    assert os.path.isdir("info202")
    shutil.rmtree("info202")
    os.remove("info202.zip")

def test_missing():
    info202data.get_module_2("foo")
