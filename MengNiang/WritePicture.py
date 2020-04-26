import json
import os
import random
import time
from urllib import request
import requests
from bs4 import BeautifulSoup

cache_json_path = os.getcwd() + "/json/PictureList"

url_host = 'http://moe.005.tv/'
test_url = 'http://moe.005.tv/78464.html'
test_url_no_next = 'http://moe.005.tv/80483.html'

file_name = 'test'
picture_dir = os.getcwd() + "/picture"
loop_index = 0


def write_picture(url):
    global loop_index
    loop_index = loop_index + 1
    print(url)
    print(loop_index)

    file_dir = picture_dir + "/" + file_name.replace('/', '_')
    if not os.path.isdir(file_dir):
        print(file_dir)
        os.mkdir(file_dir)
    picture_name = url[url.rindex('/') + 1:len(url)]
    picture_path = file_dir + '/' + picture_name
    print(picture_path)
    if os.path.isfile(picture_path):
        print('The {} already exists.'.format(picture_name))
        return
    time.sleep(random.randint(5, 9))
    try:
        request.urlretrieve(url, picture_path)
    except ConnectionResetError as e:
        print("Error!!! Connection reset by peer")
        loop_retrieve(url, picture_path)


def loop_retrieve(url, picture_path):
    try:
        time.sleep(10)
        request.urlretrieve(url, picture_path)
    except ConnectionResetError as e:
        loop_retrieve(url, picture_path)


def handle_span(spans):
    """<span style="color:#ff0000;"><span style="font-size:12px;"><img alt="" src="http://www.005.tv/uploads/allimg/190710/66-1ZG0144923638.jpg" style="width: 800px; height: 450px;"/><br/>
	ID=</span></span>"""

    for span in spans:
        if len(span.select('img')) > 0:
            img = span.select('img')[0]['src']
            write_picture(img)


def handle_img(imgs):
    for img in imgs:
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
        handle_span(spans)
        handle_img(imgs)
        next_html = soup.select(
            'body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.content_nr > div.fenye > div > ul')

        if len(next_html) > 0:
            print(next_html[0])
            print('\n')
            a_list = next_html[0].select('a')
            print(a_list)
            print('\n')

            index = 0
            size = len(a_list)
            for a in a_list:
                if index == size - 1:
                    break
                next_url = url_host + a['href']
                read_info_html_next(next_url)
                index = index + 1
        # 一种情况
        handle_img_exc_01(soup)
        handle_img_next_exc_01(soup)


def handle_img_exc_01(soup):
    imgs = soup.select(
        'body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.content_nr > div:nth-child(4) > img')
    for img in imgs:
        print(img['src'])


def handle_img_next_exc_01(soup):
    nexts = soup.select(
        'body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.fenye > div > ul')
    if len(nexts) > 0:
        a_list = nexts[0].select('a')
        print(a_list)
        index = 0
        size = len(a_list)
        for a in a_list:
            if index == size - 1:
                break
            next_url = url_host + a['href']
            read_info_html_next_exc_01(next_url)
            index = index + 1


def read_info_html_next_exc_01(url):
    req_request = requests.get(url)
    if req_request.status_code == 200:
        html_str = req_request.content.decode('utf-8')
        soup = BeautifulSoup(html_str, "html.parser")
        imgs = soup.select(
            'body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div.content_nr > div > img')
        for img in imgs:
            write_picture(img['src'])


def read_info_html_next(url):
    print(url)
    req_request = requests.get(url)
    if req_request.status_code == 200:
        html_str = req_request.content.decode('utf-8')
        soup = BeautifulSoup(html_str, "html.parser")
        spans = soup.select(
            "body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div > span")
        imgs = soup.select(
            "body > div.nav_warp > div.nav_w_left > div.content_box > div:nth-child(4) > div > img")
        handle_span(spans)
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
        # break


# read_json()
if not os.path.isdir(picture_dir):
    os.mkdir(picture_dir)

read_json()
# read_info_html("http://moe.005.tv/77602.html")

# content = '2019-04-04_Fate/GrandOrder 每日P站手机电脑壁纸推荐'
# content = content.replace('/', '_').replace(' ', '_')
# print(content)
