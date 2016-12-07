#-*-coding:utf-8 -*-
import time, threading,os
from PPP_project import cat_main,data_main
def CatThread():
    CAT=cat_main.CatMain()
    CAT.cat_main()

def DataThread():
    #time.sleep(10)       #为了保证在url中有url
    DATA=data_main.DataMain()
    DATA.data_main()

if __name__=='__main__':
    catT = threading.Thread(target=CatThread, name='CatThread')    #定义目录处理线程
    dataT= threading.Thread(target=DataThread, name='DataThread')  #定义数据网页处理线程

    print "%s running!"%threading.current_thread().name
    #catT.start()
    #catT.join()

    dataT.start()
    dataT.join()
    print "%s is ended!" % threading.current_thread().name
