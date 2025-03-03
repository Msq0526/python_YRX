import requests
from lxml import etree

url = 'http://www.yudi001.cn/wordpress/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers).text
html = etree.HTML(response)
html = html.xpath('')

print(html)
