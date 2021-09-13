
#从豆瓣电影获取首页数据
import urllib.request
url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'
}

req =urllib.request.Request(url=url,headers=headers)
urlopen = urllib.request.urlopen(req)

read = urlopen.read().decode('utf-8')
print(read)

fp=open('douban.json','w',encoding='utf-8')
fp.write(read)