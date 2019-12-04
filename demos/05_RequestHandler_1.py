#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Evan'
__time__ = '2019/12/4 11:31'

"""
RequestHandler生命周期模拟底层实现
"""


class BaseHandler(object):
    def initialize(self, *args, **kwargs):
        print('BaseHandler 初始化')

    def get(self, *args, **kwargs):
        raise Exception(405)

    def post(self):
        raise Exception(405)

    def on_finish(self):
        print('BaseHandler 释放资源')


class IndexHandler(BaseHandler):
    def initialize(self, conn):
        print(conn)
        print('调用子类 Index 初始化',)

    def get(self):
        print('调用子类 GET 请求处理')

    def on_finish(self):
        print('IndexHandler 请求释放资源')


if __name__ == '__main__':
    urlpatterns = [(r'/', IndexHandler, {'hello': '123'})]
    path = '/'
    method = 'get'
    for url in urlpatterns:
        p, c, k = url
        if path == p:
            h = c()
            h.initialize(k)
            getattr(h, method)()
            h.on_finish()


