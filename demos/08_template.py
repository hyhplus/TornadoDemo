#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/4 17:03
"""
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os


class IndexHandler(RequestHandler):
    def get(self):
        settings = {
            'username': 'Tornado-1.6.0',
            'datetime': '2019/12/12 12:23:45'
        }
        self.render('index.html', **settings)


app = Application([
    (r'/', IndexHandler)
], template_path=os.path.join(os.getcwd(), 'templates'), debug=True)

app.listen(8888)

IOLoop.current().start()


