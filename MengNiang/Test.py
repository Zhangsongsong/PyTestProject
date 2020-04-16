import os
import json

import requests
from bs4 import BeautifulSoup

# 萌娘资源 （电脑壁纸）
home_url = 'http://moe.005.tv/moeimg/bz/'

"""
json 文件夹为
"""
home_dir = os.getcwd()

json_dir = home_dir + "/json"


def write_picture_json(file_name, date, title, url):
    print(file_name)
    """写入json"""
    if not os.path.isdir(json_dir):
        os.makedirs(json_dir)
    json_path = json_dir + "/" + file_name
    if os.path.isfile(json_path):
        os.remove(json_path)
    fd = open(json_path, "w+", encoding='utf-8')
    fd.write('{\"url\":\"%s\",\"date\":\"%s\",\"title\":\"%s\",\"content\":[]}' % (url, date, title))
    fd.close()


cache_path = home_dir + "/cache"


def write_loop_cache(index, date, title, url):
    # if not os.path.isfile(cache_path):
    #     fd = open(cache_path, "w+", encoding='utf-8')
    #     fd.close()
    cache_file = open(cache_path, 'r+')
    cache_content = cache_file.read()
    cache_file.close()
    content_json = json.load(cache_content)
    content_json['index'] = index
    content_json['date'] = date
    content_json['title'] = title
    content_json['url'] = url

    cache_w = open(cache_path, 'r+')
    cache_w.write(json.dumps(content_json))
    cache_w.close()


"""
<li>
<a href="http://moe.005.tv/80483.html" target="_blank"><span class="zt_pic" style="background-image:url(http://www.005.tv/uploads/allimg/200401/66-200401164U50-L.jpg);"><img src="http://www.005.tv/uploads/allimg/200401/66-200401164U50-L.jpg"/><em>崩坏3电脑壁纸1080P</em></span></a>
<span class="zt_dep">
<strong><a href="http://moe.005.tv/80483.html">崩坏3电脑壁纸1080P</a></strong>
<dl>
<dt>2020-04-01</dt>
<dd><i class="iconfont"></i>120</dd>
</dl>
<p>崩坏3rd游戏电脑壁纸1080P...</p>
</span>
</li>
"""


def get_picture_list_by_pager(url):
    print(url)
    req_result = requests.get(url)
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup(html_str, "html.parser")
        ul = soup.select("body > div.nav_warp > div.nav_w_left > div.zhuti_w_list > ul > li")
        for li in ul:
            # 日期
            date = li.select('dl > dt')[0].text
            # 标题
            title = li.a.text
            # 文件名
            file_name = date + "_" + title
            href = li.a.attrs['href']
            write_picture_json(file_name, date, title, href)
            break


def loop_pager():
    """ http://moe.005.tv/moeimg/bz/list_4_1.html """

    for i in range(1, 100):
        main_url = 'http://moe.005.tv/moeimg/bz/list_4_{}.html'.format(i)
        get_picture_list_by_pager(main_url)
        break


loop_pager()
