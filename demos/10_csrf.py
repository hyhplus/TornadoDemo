#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/5 11:03
"""
from tornado.web import *
from tornado.ioloop import IOLoop
import os


class IndexHandler(RequestHandler):
    def get(self):
        self.render('csrf.html')

    def post(self):
        username = self.get_argument('username')
        if username:
            self.write(username)


# 配置Application的参数xsrf_cookies=True, 即开启csrf防跨域攻击
app = Application([
    (r'^/$', IndexHandler)
], template_path=os.path.join(os.getcwd(), 'templates'), xsrf_cookies=True)

app.listen(8888)

IOLoop.current().start()
