import requests
from lxml import etree
import time


url = 'https://movie.douban.com/subject/1292052/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Cookie':'bid=OcP7wGcflI8; douban-fav-remind=1; ap_v=0,6.0; ll="108288"'
}

response = requests.get(url, headers=headers, timeout=5)
html = etree.HTML(response.text)
span_property = html.xpath("//span[@class='short']/text()")
print(span_property,type('span_property'))