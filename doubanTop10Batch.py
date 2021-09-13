import urllib.parse
import urllib.request
# 创建request 2
def get_request(page):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'

    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
}
    data = {
        'page_limit': 20,
        'page_start': (page - 1) * 20
    }
    urlencode = urllib.parse.urlencode(data)
    url=url+urlencode
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):

    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_content(page,content):
    print(content)
    fp=open('douban_hot_'+str(page)+'.json','w',encoding='utf-8')
    fp.write(content)


if __name__ == '__main__':
    start_page = input('请输入开始页数')
    end_page = input('请输入结束页数')

    for page in range(int(start_page), int(end_page) + 1):
        request = get_request(page)
        content = get_content(request)
        download_content(page,content)
