import bs4 as BeautifulSoup4
import requests as requests


home_url = 'https://www.mhqwe.xyz.com'
test_url = 'https://www.baidu.com'


def get_home_pager(url):
    req_result = requests.get(url)
    if req_result.status_code == 200:
        html_str = req_result.content.decode("utf-8")
        soup = BeautifulSoup4(html_str,'html.parser')
        print(soup)


get_home_pager(test_url)
