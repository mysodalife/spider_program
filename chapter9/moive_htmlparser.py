# -*- coding: utf-8 -*-
# @Time         : 2018/10/21 17:30
# @Author       : sodalife
# @File         : moive_htmlparser.py
# @Description  : 解析html
'''
1. 提前挡墙正在上映的电影
2. 从动态加载的链接中提前我们所需要的字段
'''

import re
import json


class HtmlParser(object):

    def parse_url(self, response):
        '''
        提取正在上映的电影链接
        :param response: 返回的映射
        :return: 所有正在上映电影的链接
        '''
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls is None:
            return None
        else:  # 注意到url 一定要去重
            return list(set(urls))

    def parser_json(self, page_url, response):
        '''
        从动态链接中提取我们想要的字段
        :param page_url: 请求的url
        :param response: 返回的文字
        :return:
        '''
        pattern = re.compile(r'=(.*?);')  # 取出之间的字符串
        result = pattern.findall(response)[0]  # 获取到第一个得到的
        if result != None:
            value = json.loads(result, encoding='utf-8')  # 获取到获得的json文件
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print(e)
                return None
            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)  # 已经上映了
                else:
                    return self._parser_no_release(page_url, value, isRelease=2)  # 即将上映
            else:
                return self._parser_no_release(page_url, value)  # 还有很久才上映

    def _parser_release(self, page_url, value):
        '''
        解析已经上映的影片
        :param page_url: 请求的页面的url
        :param value: 获取到的json数据
        :return
        '''
        try:
            isRelease = 1  # 将已经上映的系统
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')
            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            if boxOffice is not None:
                TotalBoxOffice = boxOffice.get('TotalBoxOffice')
                TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
                if TotalBoxOfficeUnit == '万' or TotalBoxOfficeUnit == '亿':
                    TodayBoxOfficeUnit = 'thousand'
                TodayBoxOffice = boxOffice.get('TodayBoxOffice')
                TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')
                if TodayBoxOfficeUnit == '万' or TodayBoxOfficeUnit == '亿':
                    TodayBoxOfficeUnit == 'thousand'
                ShowDays = boxOffice.get('ShowDays')
            else:
                TotalBoxOffice = 'Unknown'
                TotalBoxOfficeUnit = ''
                TodayBoxOffice = 'Unknown'
                TodayBoxOfficeUnit = ''
                ShowDays = 0
            try:
                Rank = boxOffice.get('Rank')
            except Exception as e:
                Rank = 0
            return (
                MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal, Usercount,
                AttitudeCount, TotalBoxOffice + TotalBoxOfficeUnit, TodayBoxOffice + TodayBoxOfficeUnit, Rank, ShowDays,
                isRelease)
        except Exception as e:
            print(e, page_url, value, movieTitle)
            return None

    def _parser_no_release(self, page_url, value, isRelease=0):
        '''
        解析没有上映的电影的信息
        :param page_url: 请求的Url
        :param value: 获得的json数据
        :param isRelease: 是否上映 默认值是0
        :return:
        '''
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')
            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                Rank = 0
            return (
                MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal, Usercount,
                AttitudeCount, u'无', u'无', Rank, 0, isRelease)
        except Exception as e:
            print(e, page_url, value)
            return None
