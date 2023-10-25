import os
from urllib import request

import bs4 as BeautifulSoup4
import requests
import urllib3

urllib3.disable_warnings()

content_dir = os.getcwd() + "/content"

home_url = 'https://www.mhqwe.xyz'

# https://www.mhqwe.xyz/?searchType=0&page.currentPage=3&orderType=3&subjectName=&filmName=

is_local = False
link_book_key = '2dZpfU4Au0w8eRpvpK5IfQ=='
link_book_id = 1497
link_book_path = 6


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
            content = item.select('div > div.p-b-15.p-l-5.p-r-5')
            file_name = item.select('div > div.p-b-15.p-l-5.p-r-5 > span')[0].text
            print(file_name)
            file_dir = os.getcwd() + "/content/" + file_name
            if not os.path.isdir(file_dir):
                os.mkdir(file_dir)

            print('-------')


def get_title(soup):
    # 获取标题
    titles = soup.select("#div_width")[0].text.split('\n')
    for title in titles:
        if title.find('-') >= 0:
            return title.strip()


def read_and_write(url, dir_name):
    html_str = ''
    if is_local:
        file_r = open(os.getcwd() + "/html/cartoon_info_2", 'r+')
        html_str = file_r.read()
        file_r.close()
        dir_name = '秘密教学'
    else:
        req = requests.get(url)
        if req.status_code == 200:
            html_str = req.content.decode('utf-8')
    soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')

    # 总漫画名
    file_dir_name = dir_name
    if dir_name is None:
        file_dir_name = soup.select('#div_width > a > h3')[0].text

    current_dir = os.getcwd() + '/content/' + file_dir_name
    if not os.path.isdir(current_dir):
        os.mkdir(current_dir)
    # 多少话
    skits_name = get_title(soup).strip()
    print(skits_name)
    skits_dir = current_dir + "/" + skits_name
    if not os.path.isdir(skits_dir):
        os.mkdir(skits_dir)

    img_list = soup.select('#imgList > img')
    index = 1
    for img in img_list:
        pic_url = img.get('src')
        if pic_url is None or pic_url == '/data/jzz.png':
            pic_url = img.get('data-original')
        print(pic_url)
        pic_last_name = pic_url.split('.')[-1]
        img_path = skits_dir + "/" + "{:0>3}".format(index) + '.' + pic_last_name
        print(img_path)
        if not os.path.isfile(img_path):
            try:
                request.urlretrieve(pic_url, img_path)
            except ConnectionResetError as e:
                print("Error!!! Connection reset by peer")
                urllib3.request.urlretrieve(pic_url, img_path)
            # time.sleep(random.randint(1, 2))
        index = index + 1
    # link_id = soup.select('#div_width > p > a.button')[1].get('onclick').split(',')[1]
    # _next = link_id[1:len(link_id) - 1]
    # print(_next)
    # # 替换linkId
    # next_url = home_url + "/play?linkId=" + _next + "&bookId=" + str(link_book_id) + "&path=" + str(
    #     link_book_path) + "&key=" + link_book_key
    print(skits_name)
    # if not is_local:
    #     read_and_write(next_url, file_dir_name)


# 001 https://www.mhqwe.xyz/play?linkId=2182652&bookId=1497&path=6&key=2dZpfU4Au0w8eRpvpK5IfQ==
# 002 https://www.mhqwe.xyz/play?linkId=2182653&bookId=1497&path=6&key=yLl2mhX9YZchipZZnxUOhQ==
# 003 https://www.mhqwe.xyz/play?linkId=2182654&bookId=1497&path=6&key=ht20R2R5y+inYi83EUiotw==
# 004 https://www.mhqwe.xyz/play?linkId=2182655&bookId=1497&path=6&key=reCjq9seujn4mrMm0bDpyA==
# 005 https://www.mhqwe.xyz/play?linkId=2182656&bookId=1497&path=6&key=viBjOxkcum5iiyZefS1/Sw==
# 006 https://www.mhqwe.xyz/play?linkId=2182657&bookId=1497&path=6&key=3IAAB/RjR7NiuyDFAIj1VQ==
# 007 https://www.mhqwe.xyz/play?linkId=2182658&bookId=1497&path=6&key=bLIGgUnv2L2ilfDmJjMqcA==


#
#
#
#

current_url = 'https://www.mhqwe.xyz/play?linkId=1525998&bookId=1513&path=6&key=+aa97S7YgQj2m6Qf7i8GJA=='
read_and_write(current_url, dir_name=None)

# get_home_page(home_url)

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
