# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import threading,time
import re
lock = threading.Lock()

class CatAnalysis(object):
    def __init__(self):
        self.pattern = r",\"PROJ_RID\":\"(.+?)\","

    def cat_analysis(self,CATcontent):
        part_urls = list()

        content = re.findall(self.pattern, str(CATcontent))

        if content == None:
            print "正则失败！"
            return None
        else:
            for m in content:
                part_urls.append(m)

        return part_urls
