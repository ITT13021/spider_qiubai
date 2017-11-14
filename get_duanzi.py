# coding=utf-8
import urllib
import urllib2

import re

import sys

reload(sys)
sys.setdefaultencoding('utf8')


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div\sclass="content">\n.*\n*(.*)')
    items = re.findall(pattern, content)
    i = 1
    for item in items:
        print "第" + str(i) + "个: " + str(item) + "\n"
        i=int(i)
        i = i + 1
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
