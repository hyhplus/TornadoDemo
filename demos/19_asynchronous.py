#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 14:17
"""
import tornado.web
import tornado.ioloop
import os

"""
异步服务器端处理方式1
"""


class IndexHandler(tornado.web.RequestHandler):
    def get(self, filename):
        BaseDir = os.path.join(os.getcwd(), 'static', 'images')
        file = os.path.join(BaseDir, filename)

        content = None

        with open(file, 'rb') as fr:
            content = fr.read()

        if not content:
            self.write_error(404)
        else:
            self.set_header('Content-Type', 'image/png')
            self.write(content)

        self.finish()  # asychronous 方式支持长连接，需要手动结束请求才能返回响应


app = tornado.web.Application([
    (r'/static/(.*)', IndexHandler)
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()


