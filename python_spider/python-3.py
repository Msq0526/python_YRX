import requests
from lxml import etree

url = 'https://movie.douban.com/subject/1292052/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

data_yemian = requests.get(url, headers=headers, timeout=5).text

html = etree.HTML(data_yemian)
html_shuju = html.xpath('//span[@class="short"]/span/text()')[0].strip()
html_shuju_1 = html.xpath('//span[@class="short"]/span/text()')[1].strip()
print(html_shuju)
print(html_shuju_1)
