# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:47:11 2017

@author: gh

无翻页版本。收集内容只有第一页的30条
"""
##HTML如何提取关键字

from bs4 import BeautifulSoup   #导入bs4库
import urllib2   # 网络访问模块
import sys   

type = sys.getfilesystemencoding()  

#设置代理
#防止经常刷新页面造成页面访问被拒绝
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


#发送请求
request = urllib2.Request("https://news.ycombinator.com/newest")
#print response.read()

#回传接收到的网页信息
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"

soup = BeautifulSoup(response.read())
#print soup.prettify()    #格式化输出
#html = '<a class="storylink" href="https://insideclimatenews.org/news/31082017/climate-change-georgia-peach-harvest-warm-weather-crop-risk-farmers" rel="nofollow">In Georgia, warmer winters means peaches crops are dying</a>'
#soup = BeautifulSoup(html)

tags = soup.find_all('a',class_='storylink',rel='nofollow')
'''
下端代码参考
http://www.itkeyword.com/doc/8874465028945577x884/python-html
'''                
news_list = []
for tag in tags:
    news_dict = {}
    news_dict['News_title'] = tag.string
    news_dict['News_url'] = tag.get('href')
    news_list.append(news_dict)

file=open('After_Keyword_extraction.txt','w') 

for i in news_list:  
    if 'deep learning' in i.get('News_title') or'Deep Learning' in i.get('News_title'):
        file.write(str(i)+'\n')

print 'results successfully stored in the file'
file.close()
 