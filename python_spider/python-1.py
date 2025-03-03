import requests
from bs4 import BeautifulSoup

url = 'https://ssr1.scrape.center/'

headers = {
    'Uesr=Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 '
                  'Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


def data_c():
    for data_class in soup.find_all('h2', {'class': 'm-b-sm'}):
        print(data_class.text.strip())


# data_c()


def data_s():
    for data_span in soup.find_all('span'):
        print(data_span.text.strip())


data_s()


#     with open('dianying.txt', 'a+', encoding='utf-8') as f:
#         f.write(str(data_all.text.strip()))
#
# f.close()
def data_u():
    for data_src in soup.find_all(['div', 'span'], {'span': 'data-v-7f856186'}):
        print(data_src.text)


# data_u()

print('执行完毕！！')
