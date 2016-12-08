#-*-coding:utf-8 -*-
import urllib2

class DownData(object):
    def __init__(self):
        pass
    def download_data(self,now_url):
        try:
            request = urllib2.Request(now_url)
            response = urllib2.urlopen(request, timeout=30)
            s = response.read()
        except urllib2.URLError,e:
            print "Can't download data page:"+now_url
            return None

        return s
