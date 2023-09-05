import bs4 as BeautifulSoup4
import requests

import urllib3

urllib3.disable_warnings()

home_url = 'https://www.mhqwe.xyz.com'
test_url = 'https://www.baidu.com'

test_url_1 = 'https://www.mhqwe.xyz/play?linkId=2082973&bookId=1905&path=6&key=bNMFOi7DIVMv8kk7C8bz0A=='


def get_home_pager(url):
    req_result = requests.get(url, verify=False)
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
        # print(soup)
        img_list = soup.select("#imgList")
        print(img_list)


get_home_pager(test_url_1)
