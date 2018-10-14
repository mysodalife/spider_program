# -*- coding: utf-8 -*-
# @Time         : 2018/10/13 20:04
# @Author       : sodalife
# @File         : URLManager.py
# @Description  : 主节点的URL管理进程
# 主从模式下的 主节点的URL管理器 负责将URL的管理和将URL分配到从节点
import pickle  # 序列化 将对象变成可以传输或存储的内容，而不仅仅是基本类型的
import hashlib


class URLManager(object):
    '''
    old_urls 是利用md5压缩存储过后的
    new_urls 是直接来进行存储的
    '''

    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')
        self.old_urls = self.load_progress('old_urls.txt')

    def load_progress(self, fileName: str):
        print(f'[+] 从文件加载进度 {fileName}')
        try:
            with open(fileName, 'rb') as f:
                temp = pickle.load(f)
                return temp
        except Exception as e:
            print(f'[!] 加载文件失败 {fileName}')
        return set()

    def save_progress(self, fileName: str, data):
        with open(fileName, 'wb') as f:
            pickle.dump(data, f)

    def has_new_url(self):
        return self.new_url_size() != 0

    def get_new_url(self):
        if not self.has_new_url():
            return None
        new_url = self.new_urls.pop()
        md5 = hashlib.md5()
        md5.update(new_url)
        self.old_urls.add(md5.hexdigest())
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        md5 = hashlib.md5()
        md5.update(url)
        if url not in self.new_urls and md5.hexdigest() not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)
