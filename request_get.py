import requests


url='http://www.baidu.com/s'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
}
data={
'wd':'springcloudgateway'
}
response = requests.get(url=url,params=data,headers=headers)
response.encoding='utf-8'
print(response.text)