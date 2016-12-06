# -*-coding:utf-8 -*-
import urllib2
import requests

class DownCat(object):
    def __init__(self):
        pass
    def download_cat(self,num):
        try:
            num=str(num)
            cat_url="http://www.cpppc.org:8082/efmisweb/ppp/projectLivrary/getPPPList.do?tokenid=null"
            my_files={'queryPage':(None,num)}
            response=requests.post(cat_url,files=my_files)
            CATcontent=response.content
        except urllib2.URLError,e:
            print "Category downlaod error!\n"
            return None
        return CATcontent


