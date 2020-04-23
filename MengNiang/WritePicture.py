import json
import os

cache_json_path = os.getcwd() + "/json/PictureList"


def read_info_html():
    return


def read_json():
    print(cache_json_path)

    file_r = open(cache_json_path, 'r+')
    file_content = file_r.read()
    file_r.close()
    item_list = json.loads(file_content)
    for item in item_list:
        print(item['index'])
        print(item['date'])
        print(item['title'])
        print(item['url'])
        break


read_json()
