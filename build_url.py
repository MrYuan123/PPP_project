#-*-coding:utf-8 -*-
import urllib,sys
f
class BuildUrl(object):
    def __init__(self):
        pass
    def build_url(self,part_url):
        common_url="http://www.cpppc.org:8082/efmisweb/ppp/projectLivrary/getProjInfo.do?projId="
        final_url=common_url+urllib.quote(part_url.decode(sys.stdin.encoding).encode('utf-8'))
        return final_url

