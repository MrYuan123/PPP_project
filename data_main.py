#-*-coding:utf-8 -*-
from PPP_project import data_store,build_url,download_data,data_analysis
import threading,time
lock = threading.Lock()

class DataMain(object):
    def __init__(self):
        self.BuildUrl=build_url.BuildUrl()
        self.DownData=download_data.DownData()
        self.Dana=data_analysis.DataAnalysis()
    def data_main(self):
        print 'Enter data thread!'
        URLF=open("url_lists.md","r")
        url_lists =  URLF.readlines()

        for now_url in url_lists:

            with open("data_page_flag.md","w") as flagF:    #记录url运行的位置
                    flagF.write(now_url)

            data_page=self.DownData.download_data(now_url)

            if data_page== None:                    #对异常进行处理
                with open("error_data.md", "a") as ES:
                    ES.write(str(now_url))
                    ES.write("\n")
            else:
                if self.Dana.data_analysis(data_page)== None:    #判断是否数据处理成功的依据
                    print "Data analysis error!"
                    with open("error_data.md","a") as ES:
                        ES.write(str(now_url))
                        ES.write("\n")
                else:
                    print "Data page analysis success:%s"%now_url
        URLF.close()

        print "%s is ended!" % threading.current_thread().name
        return True