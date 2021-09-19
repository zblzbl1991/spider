import time

from lxml import etree
import urllib.request
from concurrent.futures import ThreadPoolExecutor

def get_request(page):
    url='https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
    if(page!=1):
        url='https://sc.chinaz.com/tupian/xingganmeinvtupian_'+str(page)+'.html'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def down_load(url,filename):
    print(url,filename)
    urllib.request.urlretrieve(url=url, filename='./pic/' + filename + '.jpg')
def get_content(request):
    urlopen = urllib.request.urlopen(request)
    decode = urlopen.read().decode('utf-8')
    html = etree.HTML(decode)
    altList = html.xpath('//div[@id="container"]//a//img//@alt')
    src2List = html.xpath('//div[@id="container"]//a//img//@src2')

    executor = ThreadPoolExecutor(max_workers=8)
    for i in range(len(altList)):
        name =altList[i]
        src=src2List[i]
        url_prefix='https:'
        url = url_prefix + src
        # print(name,url)
        executor.submit( down_load,url,name)
    time.sleep(4)
    # urllib.request.urlretrieve()

if __name__ == '__main__':
    # start_page = input('请输入开始页数')
    # end_page = input('请输入结束页数')
    start_page = 1
    end_page = 1
    for page in range(int(start_page), int(end_page) + 1):
        request = get_request(page)
        content = get_content(request)
        # download_content(page,content)