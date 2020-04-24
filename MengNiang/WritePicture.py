import json
import os
import requests
from bs4 import BeautifulSoup

cache_json_path = os.getcwd() + "/json/PictureList"

test_url = 'http://moe.005.tv/78464.html'


def read_info_html(url):
    req_request = requests.get(url)
    if req_request.status_code == 200:
        html_str = req_request.content.decode('utf-8')
        soup = BeautifulSoup(html_str, "html.parser")
        div = soup.select(
            "body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.content_nr > div:nth-child(1)")
        print(div)
        print('\n')
        # for img in div:
        #     print(img.src)


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
        read_info_html(item['url'])
        break


# read_json()
read_info_html(test_url)
