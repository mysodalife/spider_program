# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 17:34
# @Author       : sodalife
# @File         : Spider_Dataoutput
# @Description  : 爬虫信息的存储器

# 通过API爬虫
import codecs


class SpiderDataOutput(object):

    def __init__(self):
        self.filepath = 'kuwo.html'
        self.output_head(self.filepath)
        self.datas = []

    def output_head(self, filepath: str):
        '''
        将文件的html 头写入文件
        :param filepath: 文件路径
        :return:
        '''
        fout = codecs.open(filepath, 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.close()

    def output_html(self, path, datas):
        '''
        将文件存储到整个html 中
        :param path: 文件路径
        :param datas: 存储的数据
        :return:
        '''
        if datas is None:
            return
        fout = codecs.open(path, 'a', encoding='utf-8')
        for data in datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % (data['file_id']))
            fout.write('<td>%s</td>' % (data['name']))
            fout.write('<td>%s</td>' % (data['file_path']))
            fout.write('</tr>')
        fout.close()

    def output_end(self, path):
        '''
        输出 html 结束
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
