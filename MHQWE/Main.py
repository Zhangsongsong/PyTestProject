import os

import bs4 as BeautifulSoup4
import requests
import urllib3

urllib3.disable_warnings()

content_dir = os.getcwd() + "/content"

home_url = 'https://www.mhqwe.xyz'

# https://www.mhqwe.xyz/?searchType=0&page.currentPage=3&orderType=3&subjectName=&filmName=

start_index = 0
is_local = True


def get_home_page(url):
    html_str = ''
    if is_local:
        local_url = os.getcwd() + "/html/Home"
        file_r = open(local_url, 'r+')
        html_str = file_r.read()
        file_r.close()
    else:
        req = requests.get(url)
        if req.status_code == 200:
            html_str = req.content.decode("utf-8")
    soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
    pages = soup.select('#app > div.wrapper > div > div.col-xs-12')
    print(len(pages))
    for page in pages:
        items = page.select('div > div.col-xs-6.col-sm-6.col-md-4.col-lg-2.list-col')
        print(len(items))
        for item in items:
            print(item.select('div > div.p-b-15.p-l-5.p-r-5 > span')[0].text)
            print('-------')


get_home_page(home_url)

#
# def get_home_pager(url):
#     req_result = requests.get(url, verify=False)
#     if req_result.status_code == 200:
#         html_str = req_result.content.decode("utf-8")
#         soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
#         next_html = soup.select("#div_width > p")[2]
#         next_key = next_html.select("a")[1].attrs['onclick']
#         # openMH('1905','2082974',6)
#         tmp_1 = next_key.index('(')
#         values = next_key[tmp_1:]
#         print(values)
#
#
# def get_page(url):
#     req_result = requests.get(url, verify=False)
#     if req_result.status_code == 200:
#         html_str = req_result.content.decode("utf-8")
#         soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
#         # print(soup)
#         img_list = soup.select("#imgList")
#         # title = get_title(soup)
#         # 创建目录
#         check_and_create_file_dir(soup)
#
#
# def check_and_create_file_dir(soup):
#     file_name = get_file_name(soup)
#     file_dir = content_dir + "/" + file_name
#     if not os.path.isdir(file_dir):
#         print(file_dir)
#         os.mkdir(file_dir)
#
#
# def get_file_name(soup):
#     return soup.select("#div_width > a > h3")[0].text
#
#
# def get_title(soup):
#     # 获取标题
#     titles = soup.select("#div_width")[0].text.split('\n')
#     for title in titles:
#         if title.find('-') >= 0:
#             return title.strip()
#
#
# def get_next(soup):
#     next_html = soup.select("#div_width > p")[2]
#     next_key = next_html.select("a")[1].attrs['onclick']
#     # openMH('1905','2082974',6)
#     tmp_1 = next_key.index('(')
#     values = next_key[tmp_1:]
#     print(values)
#
#
# get_page(test_url_1)
