# -*- coding: utf-8 -*-
# @Time         : 2018/10/13 13:36
# @Author       : sodalife
# @File         : DataOutput.py
# @Description  : 数据存储器
import codecs  # 解决编码问题


class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        '''
        将数据存储到内存中 内存解析
        :param data: 存储的数据
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        '''
        解决文件不同的编码问题 使用了 codecs
        :return:
        '''
        f = codecs.open('baike.html', 'w', encoding='utf-8')  # 使用 python 编码将默认使用 ascii编码
        f.write('<html>')
        f.write('<body>')
        f.write('<table>')
        for data in self.datas:
            f.write('<tr>')
            f.write('<td>%s</td>' % data['url'])
            f.write('<td>%s</td>' % data['title'])
            f.write('<td>%s</td>' % data['summary'])
            f.write('</tr>')
        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        f.close()
