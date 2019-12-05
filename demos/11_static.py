#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/5 13:58
"""
import tornado.web
import tornado.ioloop
import os


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 在app对象指定模板根目录即可
        self.render('static.html')


app = tornado.web.Application([
    (r'/', IndexHandler),
    # 读取静态文件方式一
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.getcwd(), 'static', 'images')}),


], template_path=os.path.join(os.getcwd(), 'templates'))

# 方式二
# static_path=os.path.join(os.getcwd(), 'static', 'images')

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()


