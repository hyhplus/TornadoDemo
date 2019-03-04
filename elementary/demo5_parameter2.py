#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
混合方式：
get_arguments(...)/get_argument(...)

访问地址：
http://localhost:8000/?user=123&user=223
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        """
        获取get方式的参数
        :return:
        """
        user = self.get_arguments('user')
        print('get方式获取参数：' + str(user))

    def post(self):
        """
        获取post方式的参数
        :return:
        """
        user = self.get_argument('user')
        print('post方式获取参数：', user.encode('utf-8'))


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8000)
    IOLoop.current().start()




