import re
import requests
from bs4 import BeautifulSoup
import time


class RRS3:
    def __init__(self):
        self.url = 'https://ssr3.scrape.center/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        self.auth = ('admin', 'admin')

    #   获取数据请求函数
    def get_data_info(self, page):
        response = requests.get(self.url.format(page), headers=self.headers, auth=self.auth).text
        soup = BeautifulSoup(response, 'lxml')
        return soup.prettify()

    #   分页函数
    def page_name(self):
        for page in range(1, 11):
            print('当前获取的是第{}次。。。。。。'.format(page))
            print(self.get_data_info(page))
            time.sleep(5)


if __name__ == '__main__':
    rrs3 = RRS3()
    rrs3.page_name()
