# 导入包
import urllib.request
import urllib.response
# 添加地址
from urllib3 import HTTPResponse

url = "http://www.baidu.com"
# response: HTTPResponse = urllib.request.urlopen(url)
urllib.request.urlretrieve(url,"./down.html");
# read readline readlines read getUrl getheaders
