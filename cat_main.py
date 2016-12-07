#-*-coding:utf-8 -*-
from PPP_project import data_store,download_cat,cat_analysis,build_url
import threading,time
lock = threading.Lock()

class CatMain(object):
    def __init__(self):
        self.Dcat=download_cat.DownCat()
        self.Aana=cat_analysis.CatAnalysis()
        self.Build=build_url.BuildUrl()

    def cat_main(self):
        print "Enter cat thread!"

        with open("page_counter.md","r") as fileS:              #文件中记录目录访问的情况
            now_page=fileS.readline()

        now_page=int(now_page)                                  #对从文件中读入的字符进行强制类型转换

        while now_page<=data_store.total:
            print "now at page:%d"%now_page
            CATcontent = self.Dcat.download_cat(now_page)

            if CATcontent==None:                                #对下载不成功的网页保存页码信息
                   print "empty category!"
                   with open("error_cat.md","a") as F:
                       F.write(str(now_page))
                       F.write("\n")
            else:                                               #进入category页面处理
                page_list=self.Aana.cat_analysis(CATcontent)

                if page_list==None:
                    print "empty page_list!"

                    with open("error_cat.md", "a") as F:
                        F.write(str(now_page))
                        F.write("\n")
                else:
                    urlF=open("url_lists.md","a")

                    for part_url in page_list:     #用于将爬取的网址存在文件中
                        full_url=self.Build.build_url(part_url)
                        urlF.write(str(full_url))
                        urlF.write("\n")
                    urlF.close()

                    # 使用线程锁，保证data_store.py中的burl_list只能同时一个进程修改
                    # lock.acquire()
                    # try:
                    #     for urlMess in page_list:
                    #         data_store.url_list.append(urlMess)
                    # finally:
                    #     lock.release()

            now_page+=1

            with open("page_counter.md", "w") as fileS:          # 文件中记录目录访问的情况
                fileS.write(str(now_page))

        print "End cat thread!"
        return True












