import os

import bs4 as BeautifulSoup4
import requests

import urllib3

urllib3.disable_warnings()

content_dir = os.getcwd() + "/content"

home_url = 'https://www.mhqwe.xyz.com'
test_url = 'https://www.baidu.com'

test_url_1 = 'https://www.mhqwe.xyz/play?linkId=2082973&bookId=1905&path=6&key=bNMFOi7DIVMv8kk7C8bz0A=='

start_index = 0


def get_home_pager(url):
    req_result = requests.get(url, verify=False)
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
        next_html = soup.select("#div_width > p")[2]
        next_key = next_html.select("a")[1].attrs['onclick']
        # openMH('1905','2082974',6)
        tmp_1 = next_key.index('(')
        values = next_key[tmp_1:]
        print(values)


def get_page(url):
    req_result = requests.get(url, verify=False)
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
        # print(soup)
        img_list = soup.select("#imgList")
        # title = get_title(soup)
        # 创建目录
        check_and_create_file_dir(soup)


def check_and_create_file_dir(soup):
    file_name = get_file_name(soup)
    file_dir = content_dir + "/" + file_name
    if not os.path.isdir(file_dir):
        print(file_dir)
        os.mkdir(file_dir)


def get_file_name(soup):
    return soup.select("#div_width > a > h3")[0].text


def get_title(soup):
    # 获取标题
    titles = soup.select("#div_width")[0].text.split('\n')
    for title in titles:
        if title.find('-') >= 0:
            return title.strip()


def get_next(soup):
    next_html = soup.select("#div_width > p")[2]
    next_key = next_html.select("a")[1].attrs['onclick']
    # openMH('1905','2082974',6)
    tmp_1 = next_key.index('(')
    values = next_key[tmp_1:]
    print(values)


get_page(test_url_1)
