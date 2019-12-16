#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 14:26
"""
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.gen import coroutine
from tornado.concurrent import Future
import os


class IndexHandler(RequestHandler):
    @coroutine
    def get(self, filename):
        # 协程让特定方法完成这部分操作
        content = yield self.read_img(filename)

        if not content:
            self.write_error(404)
        else:
            self.set_header('Content-Type', 'image/jpg')
            self.write(content)

    @staticmethod
    def read_img(filename):
        base_dir = os.path.join(os.getcwd(), 'static', 'images')
        file = os.path.join(base_dir, filename)

        with open(file, 'rb') as fr:
            content = fr.read()

        # 类似于生成器中的send
        future = Future()
        future.set_result(content)

        return future


app = Application([
    (r'/static/(.*)', IndexHandler)
])

app.listen(8888)

IOLoop.instance().start()




