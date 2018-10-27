# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 16:57
# @Author       : sodalife
# @File         : Spider_parser
# @Description  : 移动端的HTML解析器

import json


class SpiderParser(object):

    def get_kw_cat(self, response):
        '''
        从返回的数据中提取出来整个name 和 id 然后再将 id 代入到连接中获取节目的详细信息
        :param response: 返回的内容
        :return:
        '''
        if response is None:
            return
        try:
            kw_json = json.loads(response)
            cat_info = []
            if kw_json['sign'] is not None:
                if kw_json['list'] is not None:
                    for data in kw_json['list']:
                        id = data['Id']
                        name = data['Name']
                        cat_info.append({'id': id, 'cat_name': name})
                    return cat_info
        except Exception as e:
            print(e)

    def get_kw_detail(self, response):
        '''
        将具体的节目信息带入
        :param response: 返回的信息
        :return: 节目的具体信息
        '''
        if response is None:
            return
        detail_json = json.loads(response)
        details = []
        for data in detail_json['Chapters']:
            if data is None:
                return
            else:
                try:
                    file_path = data['Path']
                    name = data['Name']
                    file_id = str(data['Id'])
                    details.append({'file_id': file_id, 'name': name, 'file_path': file_path})
                except Exception as e:
                    print(e)
        return details
