# 导入包
import urllib.request
import urllib.response
import urllib.parse as parse
# 添加地址
from urllib3 import HTTPResponse

url = "https://www.baidu.com/s?"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
}
data={
    'wd':'周杰伦',
    'value':'1',
    'location':'台湾'

}
urlencode = parse.urlencode(data)
print(urlencode)
# 需要注意参数顺序
req = urllib.request.Request(url=url+urlencode, headers=headers)

response: HTTPResponse = urllib.request.urlopen(req)
decode = response.read().decode('utf-8')
print(decode)
# read readline readlines read getUrl getheaders
