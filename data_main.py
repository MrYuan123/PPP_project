#-*-coding:utf-8 -*-
from PPP_project import url_store
import threading,time
lock = threading.Lock()

class DataMain(object):
    def __init__(self):
        pass
    def data_main(self):
        print 'Enter data thread!'
        lock.acquire()
        try:
            m=url_store.url_list.pop(0)
            print m
        finally:
            lock.release()
        return True