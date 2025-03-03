import requests
from lxml import etree
import csv


class ssr1:
    def __init__(self):
        self.url = 'https://ssr1.scrape.center/page/{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

    def get_info_data(self):
        data_list = []
        for page in range(1, 12):
            print('现在正在爬取第{}页！！'.format(page))
            response = requests.get(self.url.format(page), headers=self.headers, timeout=10).text
            html = etree.HTML(response)
            div_data = html.xpath('//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]')
            for div_href in div_data:
                name = div_href.xpath('a/h2/text()')[0]
                href = 'https://ssr1.scrape.center' + div_href.xpath('a/@href')[0]
                span_1 = html.xpath('//span/text()')[1]
                span_2 = html.xpath('//span/text()')[2]
                span_3 = html.xpath('//span/text()')[3]
                span_5 = html.xpath('//span/text()')[5]
                span_6 = html.xpath('//span/text()')[6]
                data_list.append([name, href, span_1, span_2, span_3, span_5, span_6])

        self.cvs_data(data_list)

    def cvs_data(self, data_list):
        with open('ssr1.json', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'href', 'span_1', 'span_2', 'span_3', 'span_5', 'span_6'])
            writer.writerows(data_list)


if __name__ == '__main__':
    SSR1 = ssr1()
    SSR1.get_info_data()
