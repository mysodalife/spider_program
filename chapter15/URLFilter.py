# -*- coding: utf-8 -*-
# @Time         : 2018/11/5 19:42
# @Author       : sodalife
# @File         : URLFilter
# @Description  : 自定义的 URLFilter
from w3lib.url import canonicalize_url
import hashlib
from pybloom_live import ScalableBloomFilter
from scrapy.dupefilter import RFPDupeFilter


class URLFilter(RFPDupeFilter):
    '''
    过滤 URL
    '''

    def __init__(self, path=None):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path=path)  # 调用父类的构造方法

    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)


class URLSha1Filter(RFPDupeFilter):
    '''
    将 url 经过 sha1 处理以后再去重
    '''

    def __init__(self, path=None):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))  # 自动给url 格式化
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_seen:  # 判断一下是否存在
            return True
        else:
            self.urls_seen.add(url_sha1)


class URLBloomFilter(RFPDupeFilter):

    def __init__(self, path=None):
        self.urls_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        RFPDupeFilter.__init__(self, path)  # 构造函数

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_sbf:
            return True
        else:
            self.urls_sbf.add(url_sha1)