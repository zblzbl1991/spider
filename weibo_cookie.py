import urllib.request

url = 'https://weibo.com/u/5474753939/home'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
    'cookie': 'SINAGLOBAL=9010645648917.912.1591972957250; UOR=hs.blizzard.cn,widget.weibo.com,www.china.com.cn; login_sid_t=2b35bbec46a8c5845ae44310c9d7d9b0; cross_origin_proto=SSL; wb_view_log=1280*8002; _s_tentry=-; Apache=6155882497918.925.1631666327614; ULV=1631666327621:15:1:1:6155882497918.925.1631666327614:1622342359178; SUB=_2A25MRTCADeRhGeNK7FYW9S3FyDWIHXVvMyVIrDV8PUNbmtAKLVbWkW9NSTLqRneRU9KVZU3mBrfiuSbhibrH1fGV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhL4PUOHpQWKv52Huy9HR9B5JpX5KzhUgL.Fo-XS0BNSKe4e0.2dJLoIXnLxKqL1-eL1h5LxKBLB.BLBoeLxKqL1--L1-eLxKMLBozL1KzLxKqLBK.L1K.LxK-LBo5L12qLxKML1-zL1hqLxK-L12qL12zt; ALF=1663202385; SSOLoginState=1631666384; wvr=6; wb_view_log_5474753939=1280*8002; webim_unReadCount=%7B%22time%22%3A1631698662431%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A19%2C%22msgbox%22%3A0%7D'
    ,'referer': 'https://weibo.com/u/5474753939/home'

}
request=urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
lines = response.read().decode('utf-8')
print(lines)
# for line in lines:
#     print(line)
