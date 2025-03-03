import requests


url = 'https://webapi.qingting.fm/api/mobile/rank/hotSaleWeekly'

headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

response = requests.get(url, headers=headers).json()

for temp in response['rankinglist']:
    new_data = dict()
    new_data['title'] = temp['title']
    new_data['data_url'] ='https://m.qingting.fm' + temp['urlScheme']
    response_1 = requests.get(url=new_data['data_url'] , headers=headers).text
    #print(new_data)
    print(response_1)
