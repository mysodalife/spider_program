# -*- coding: utf-8 -*-
# @Time         : 2018/10/14 10:39
# @Author       : sodalife
# @File         : DataOutput.py
# @Description  : 主节点的数据存取进程
import codecs
import time


class DataOutput(object):

    def __init__(self):
        self.filepath = f'baike{time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())}.html'
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_html(self, path):
        '''
        数据写入到html中
        :param path: 文件的路径
        :return:
        '''
        f = codecs.open(path, 'a', encoding='utf-8')
        for data in self.datas:
            f.write('<tr>')
            f.write('<td>%s</td>' % data['url'])
            f.write('<td>%s</td>' % data['title'])
            f.write('<td>%s</td>' % data['summary'])
            f.write('</tr>')
            self.datas.remove(data)  # 将整个移除 到10个就完整
        f.close()

    def output_head(self, path):
        '''
        输出html
        :param path: 文件路径
        :return:
        '''
        f = codecs.open(path, 'w', encoding='utf-8')
        f.write('<html>')
        f.write('<body>')
        f.write('<table>')
        f.close()

    def output_end(self, path):
        f = codecs.open(path, 'a', encoding='utf-8')
        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        f.close()
