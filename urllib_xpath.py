from lxml import etree
import urllib.request

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'
}

req = urllib.request.Request(url=url, headers=headers)
urlopen = urllib.request.urlopen(req)
# urlopen = urllib.request.urlretrieve(url,'douban.html')


read = urlopen.read().decode('utf-8')
# t = open('douban.html', 'w', encoding='utf-8')
# t.write(read)
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.HTML(read, parser)
# print(tree)
xparse = tree.xpath('//input[@id="su"]/@value')
# xparse = tree.xpath('//body//input')
print(xparse)
