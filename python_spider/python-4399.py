import requests
import json
from lxml import etree


# 创建game_4399类
class game_4399():
    def __init__(self):
        self.url = 'https://www.4399.com/flash/new_{}.htm'
        self.headers = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/131.0.0.0 Safari/537.36'
        }
        self.game_list = list()

    # html_xpath_data使用xpaht方法获取到了4399data数据
    def html_xpaht_data(self):
        for page in range(1, 11):
            print('正在打印第{}页数据！！！！'.format(page))
            print('*' * 30)
            response = requests.get(url=self.url.format(page), headers=self.headers)
            response.encoding = 'gbk'
            html = etree.HTML(response.text)
            a_data = html.xpath('//ul[@class = "n-game cf"]/li/a')
            for a in a_data:
                item = dict()
                item['name'] = a.xpath('./b/text()')[0]
                item['href'] = 'https://www.4399.com/flash' + a.xpath('./@href')[0]
                item['time'] = a.xpath('../em/text()')[0]
                self.game_list.append(item)
        return self.game_list

    def json_info_data(self, game_list):
        with open('game.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(game_list, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    game = game_4399()
    game.html_xpaht_data()
    game.json_info_data(game.game_list)
