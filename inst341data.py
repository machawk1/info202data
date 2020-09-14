import os
import zipfile
import urllib.request 

base_url = "https://github.com/edsu/inst341/raw/master/"

def get_data(rel_url):
    url = base_url + rel_url
    local_file = os.path.basename(url)
    try:
        urllib.request.urlretrieve(url, local_file)
    except:
        print("Unable to download data")
        return None

    if url.endswith('.zip'):
        z = zipfile.ZipFile(local_file)
        z.extractall()
        for info in z.infolist():
            print("downloaded {}".format(info.filename))
    else:
        print("downloaded {}".format(local_filename))

def get_module_2(username):
    get_data("modules/module-{0:02n}/data/{1:s}.zip".format(2, username))
