#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/4 17:53
"""
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os


class User(object):
    def __init__(self, name):
        self.name = name


def reverse(obj):
    if isinstance(obj, list):
        obj.reverse()
    return obj


class IndexHandler(RequestHandler):
    def get(self):
        # 对象
        user = User('Alan')
        # 列表
        lst = ['list1', 'list2', 'list3']
        # 字典
        d = {
            'username': 'Tornado-1.6.0',
            'datetime': '2019/12/12 12:23:45'
        }
        # 转义字符
        str_ = '<h4>string h4</h4>'

        self.render('index_2.html', username='xxx', user=user, lst=lst, d=d, str_=str_, r=reverse)


app = Application([
    (r'/', IndexHandler)
], template_path=os.path.join(os.getcwd(), 'templates'), debug=True)

app.listen(8888)

IOLoop.current().start()


