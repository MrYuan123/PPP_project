#-*-coding:utf-8 -*-
from PPP_project import url_store
import threading,time
lock = threading.Lock()

class CatMain(object):
    def __init__(self):
        pass
    def cat_main(self):
        print "Enter cat thread!"
        lock.acquire()
        try:
            url_store.url_list.append('1')
            url_store.url_list.append('2')
            url_store.url_list.append('3')
            url_store.url_list.append('4')
        finally:
            lock.release()
        return True