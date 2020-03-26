import os
import time
from search.index_files_parser import parse_code
import re


def get_extension(file_name: str):
    return file_name.split('.')[-1]


data_all = []


def save_to_json(json_data: dict, json_filename: str):
    """
    This is a function to save a dict or json to a .json file
    :param json_data: the Python dictionary or json data
    :param json_filename: json file to which you want to save this
    :return: None
    """
    import json
    with open(json_filename, 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def search(root, indent=0, flags=None, extension='py'):
    """
    Recursive function to index all the files in the root directory. Appends are the filepaths to list data_all
    :param root: starting directory
    :param indent: for printing in console
    :param flags: words to ignore in the path while indexing
    :param extension: file extension to index
    :return: None
    """
    if root[-1] is not '/':
        root = root + '/'

    # print(indent*"_", f"Inside the folder: {root}")
    if len(os.listdir(root)) == 0:
        return "End of indexing reached!"
    for file in os.listdir(root):
        try:
            if os.path.isdir(root + file):
                search(root + file + '/', indent + 2, flags, extension)
            file_extension = get_extension(root + file)
            if all([x not in root for x in flags] + [extension == file_extension]):
                print((indent + 2) * "_", root + file)
                result = parse_code(file_path=root + file)
                if len(result) > 0:
                    # print((indent + 3) * "_", result)
                    data_all.append(result)

        except PermissionError as permission_denied:
            print(f"Not allowed to open the following file {root + file}\n{permission_denied}")
            continue


def re_test(text: str):
    try:
        result_re = re.search(r'\"\"\"(.*?)\"\"\"', text)
        if result_re:
            print(result_re.group(1))
        else:
            print("not found")
    except Exception as e:
        print("not found", e)


if __name__ == '__main__':
    search(root='/Users/harsh/Desktop/', flags=['corepython', 'Anaconda', 'scheme', 'site-package', 'venv',
                                                       'google-cloud-sdk'])
    d = [y for x in data_all for y in x]
    json_data = {"data": d}
    save_to_json(json_data=json_data, json_filename="jsons/result.json")