import bs4 as BeautifulSoup4
import requests

import ssl

ssl_context = ssl.create_default_context()

home_url = 'https://www.mhqwe.xyz.com'
test_url = 'https://www.baidu.com'


def get_home_pager(url):
    req_result = requests.get(url, verify=False)
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup4.BeautifulSoup(html_str, 'html.parser')
        print(soup)


get_home_pager(home_url)
