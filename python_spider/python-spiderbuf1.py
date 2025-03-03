import requests
import csv
from lxml import etree


def get_html():
    url = 'https://spiderbuf.cn/playground/s04?pageno=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    # print(response)
    return response


def html_data_info():
    soup = get_html()
    if soup is None:
        return None

    HTML = etree.HTML(soup)
    h3_list = HTML.xpath('//div[@style="flex: 0 0 68%;"]/h3/text()')
    print(h3_list)

    tables = HTML.xpath('//table[@class="table"]')
    info_data = []
    # for table in tables:
    #     ths = table.xpath('//tr/th/text()')[0:]
    #     # ths1 = table.xpath('//tr/th/text()')[1]
    #     # ths2 = table.xpath('//tr/th/text()')[2]
    #     # ths3 = table.xpath('//tr/th/text()')[3]
    #     # ths4 = table.xpath('//tr/th/text()')[4]
    #     # ths5 = table.xpath('//tr/th/text()')[5]
    #     # ths6 = table.xpath('//tr/th/text()')[6]
    #     # ths7 = table.xpath('//tr/th/text()')[7]
    #     tds = table.xpath('//tr/td/text()')
    #     info_data.append(ths)
    #     info_data.append(tds)
    for table in tables:
        ths = table.xpath('.//tr[1]/th/text()')
        for row in table.xpath('.//tr')[1:]:  # 跳过表头行
            tds = row.xpath('.//td/text()')
            if len(ths) == len(tds):
                info_data.append(dict(zip(ths, tds)))
    print(info_data)


if __name__ == '__main__':
    html_data_info()