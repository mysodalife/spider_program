# -*- coding: utf-8 -*-
# @Time         : 2018/10/22 9:55
# @Author       : sodalife
# @File         : movie_dataoutput.py
# @Description  : 用来存储解析到的电影数据
import pymysql


class DataOutPut(object):

    def __init__(self):
        self.cx = pymysql.connect(host='222.199.193.65', port=3306, user='root', passwd='duhan', database='test',
                                  charset='utf8')
        self.cursor = self.cx.cursor()
        self.create_table("MTime")
        self.datas = []

    def create_table(self, table_name: str):
        '''
        创建数据库表
        :param table_name: 表名
        :return:
        '''
        values = '''
        id int primary key not null auto_increment,
        MovieId int,
        MovieTitle varchar(200) not null,
        RatingFinal float not null default 0.0,
        ROtherFinal float not null default 0.0,
        RPictureFinal float not null default 0.0,
        RDirectorFinal float not null default 0.0,
        RStoryFinal float not null default 0.0,
        Usercout int not null default 0,
        AttitudeCount int not null default 0,
        TotalBoxOffice varchar(20) not null,
        TodayBoxOffice varchar(20) not null,
        moive_rank int not null default 0,
        ShowDays int not null default 0,
        isRelease int not null default 0
        '''

        self.cursor.execute("create table if not exists %s (%s)" % (table_name, values))

    def store_data(self, data):
        '''
        添加数据
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_db("MTime")

    def output_db(self, table_name):
        '''
        将数据存储到mysql中
        :param table_name: 待存储的表名
        :return:
        '''
        for data in self.datas:
            print(data)
            self.cursor.execute(
                'insert into %s (MovieId,MovieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,RStoryFinal,Usercout,AttitudeCount,TotalBoxOffice,TodayBoxOffice,moive_rank,ShowDays,isRelease ) values (%s,"%s",%s,%s,%s,%s,%s,%s,%s,"%s","%s",%s,%s,%s)' % (
                    table_name, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                    data[9],
                    data[10], data[11], data[12], data[13]))
            # print(sen)
            # self.cursor.execute("insert into %s (MovieId,MovieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,RStoryFinal,Usercout,AttitudeCount,TotalBoxOffice,TodayBoxOffice,moive_rank,ShowDays,isRelease ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(table_name, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13]))
            self.cx.commit()
            self.datas.remove(data)

    def output_end(self):
        '''
        关闭数据库
        :return:
        '''
        if len(self.datas) > 0:
            self.output_db('MTime')
        self.cursor.close()
        self.cx.close()