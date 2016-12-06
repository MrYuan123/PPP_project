#-*-coding:utf-8 -*-
from PPP_project import data_store,build_url
import threading,time
lock = threading.Lock()

class DataMain(object):
    def __init__(self):
        self.BuildUrl=build_url.BuildUrl()
    def data_main(self):
        print 'Enter data thread!'

        while data_store.url_list:              #判断url_list中是否为空
            lock.acquire()
            try:                                #添加线程锁保证同一时间只有一个线程修改url_list
                now_part_url=data_store.url_list.pop(0)
            finally:
                lock.release()

            full_url=self.BuildUrl.build_url(now_part_url)
            print full_url

        return True