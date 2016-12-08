# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import re,csv

class DataAnalysis(object):
    def __init__(self):
        pass
    def data_analysis(self,data_page):
        soup = BeautifulSoup(data_page)
        project_name = soup.center.getText().strip()

        tables = soup.findAll('table')
        tab = tables[0]
        content_list = tab.findAll('tr')
        contentF = 0  # 用于判断当前获取的为何种信息
        otherFLAG = 0  # 标记其余信息量的多少

        content = []    #用于存储信息

        for i in range(0, 16):
            content.append(0)

        for tr in tab.findAll('tr'):
            data_list = tr.findAll('td')
            now_content = data_list[0].getText().strip()
            now_data = data_list[1].getText().strip()

            # =====================================================用list代替
            if contentF == 0:
                content[0] = now_data
            elif contentF == 1:
                content[1] = now_data
            elif contentF == 2:
                content[2] = now_data
            elif contentF == 3:
                content[3] = now_data
            elif contentF == 4:
                content[4] = now_data
            elif contentF == 5:
                content[5] = now_data
            elif contentF == 6:
                content[6] = now_data
            elif contentF == 7:
                content[7] = now_data
            elif contentF == 8:
                content[8] = now_data
            elif contentF == 9:
                content[9] = now_data
            elif contentF == 10:
                content[10] = now_data
            elif contentF == 11:
                content[11] = now_data
            elif contentF == 12:
                content[12] = now_data
            elif contentF == 13:
                content[13] = now_data
            else:
                otherFLAG += 1
                content[14] = otherFLAG
            contentF += 1
        if otherFLAG == 0:
            content[14] = None
        content[15] = project_name

        content = tuple(content)      #将content转成tuple形式

        csvfile = file('ppp_collect.csv', 'a')
        writer = csv.writer(csvfile)
        st = []                       #转成list存储的形式
        st.append(content)
        writer.writerows(st)
        csvfile.close()
        return True