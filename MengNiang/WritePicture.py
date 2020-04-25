import json
import os
from urllib import request
import requests
from bs4 import BeautifulSoup

cache_json_path = os.getcwd() + "/json/PictureList"

test_url = 'http://moe.005.tv/78464.html'

file_name = 'test'
picture_dir = os.getcwd() + "/picture"


def write_picture(url):
    print(url)
    file_dir = picture_dir + "/" + file_name
    if not os.path.isdir(file_dir):
        print(file_dir)
        os.mkdir(file_dir)
    picture_name = url[url.rindex('/') + 1:len(url)]
    picture_path = file_dir + '/' + picture_name
    print(picture_path)
    if os.path.isfile(picture_path):
        print('The {} already exists.'.format(picture_name))
        return
    request.urlretrieve(url, picture_path)


def handle_span(spans):
    """<span style="color:#ff0000;"><span style="font-size:12px;"><img alt="" src="http://www.005.tv/uploads/allimg/190710/66-1ZG0144923638.jpg" style="width: 800px; height: 450px;"/><br/>
	ID=</span></span>"""

    for span in spans:
        img = span.select('img')[0]['src']
        write_picture(img)


def handle_img(imgs):
    for img in imgs:
        print(img['src'])
        write_picture(img['src'])


def read_info_html(url):
    req_request = requests.get(url)
    if req_request.status_code == 200:
        html_str = req_request.content.decode('utf-8')
        soup = BeautifulSoup(html_str, "html.parser")
        spans = soup.select(
            "body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.content_nr > div:nth-child(1) > span")
        imgs = soup.select(
            "body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.content_nr > div:nth-child(1) > img")
        # handle_span(spans)
        handle_img(imgs)
        handle_img(imgs)


def read_json():
    print(cache_json_path)

    file_r = open(cache_json_path, 'r+')
    file_content = file_r.read()
    file_r.close()
    item_list = json.loads(file_content)
    global file_name
    for item in item_list:
        print(item['index'])
        print(item['date'])
        print(item['title'])
        print(item['url'])
        file_name = item['date'] + '_' + item['title']
        print(file_name)
        read_info_html(item['url'])
        break


# read_json()
if not os.path.isdir(picture_dir):
    os.mkdir(picture_dir)

read_json()
# read_info_html(test_url)
