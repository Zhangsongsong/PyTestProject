import os
import json

import requests
from bs4 import BeautifulSoup

# 萌娘资源 （电脑壁纸）
from info.Bean import CacheInfo

home_url = 'http://moe.005.tv/moeimg/bz/'
# 内容有多页的
pager_info_items = 'http://moe.005.tv/78464.html'

"""
json 文件夹为
"""
home_dir = os.getcwd()

# 文件记录
cache_path = home_dir + "/cache"

# 文件存储地址
file_content_path = home_dir + "/json/PictureList"

global cache_info
current_index = 0


def write_file_content(index, date, title, url):
    """ 写入文件"""
    content = "\"index\":{},\"date\":\"{}\",\"title\":\"{}\",\"url\":\"{}\"".format(index, date, title, url)
    content = "{" + content + "}"
    file_r = open(file_content_path, 'rb+')
    file_r.seek(-1, os.SEEK_END)
    file_r.truncate()
    file_r.close()

    # file_c = open(file_content,)
    size = os.path.getsize(file_content_path)
    print(size)
    is_new = False
    if 5 >= size >= 0:
        is_new = True
    file_w = open(file_content_path, 'a+', encoding='utf-8')
    if not is_new:
        file_w.write(',' + content + ']')
    else:
        file_w.write(content + ']')
    file_w.close()


def write_loop_cache():
    """写入缓存"""
    s = json.dumps(obj=cache_info.__dict__, ensure_ascii=False)
    print(s)
    cache_w = open(cache_path, 'w+')
    cache_w.write(s)
    cache_w.close()


def get_picture_list_by_pager(url):
    print(url)
    req_result = requests.get(url)
    global current_index
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup(html_str, "html.parser")
        ul = soup.select("body > div.nav_warp > div.nav_w_left > div.zhuti_w_list > ul > li")
        for li in ul:
            if cache_info.index >= current_index:
                current_index = current_index + 1
                continue

            # 日期
            date = li.select('dl > dt')[0].text
            # 标题
            title = li.a.text
            title = title.replace('\\', '')
            # 文件名
            file_name = date + "_" + title
            href = li.a.attrs['href']

            cache_info.index = cache_info.index + 1
            cache_info.date = date
            cache_info.title = title
            cache_info.url = href
            write_file_content(cache_info.index, cache_info.date, cache_info.title, cache_info.url)
            write_loop_cache()
            # break


def loop_pager():
    """ http://moe.005.tv/moeimg/bz/list_4_1.html """

    for i in range(1, 100):
        main_url = 'http://moe.005.tv/moeimg/bz/list_4_{}.html'.format(i)
        get_picture_list_by_pager(main_url)
        break


def cache_info_hook(d):
    """ dict to CacheInfo 的转换"""
    """
    index: 当前item 下标
    date: 当前item 文件时间
    title: 当前item 标题
    url: 当前item 超链接
    """
    return CacheInfo(d['index'], d['date'], d['title'], d['url'])


def init_cache_info():
    fd = open(cache_path, "r+")
    file_content = fd.read()
    fd.close()
    global cache_info
    cache_info = json.loads(file_content, object_hook=cache_info_hook)
    print(cache_info.index)


init_cache_info()
loop_pager()
