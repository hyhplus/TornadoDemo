#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 9:33
"""
from tornado.ioloop import IOLoop
from tornado.web import Application
from session_.urls import *


class HttpServer(Application):
    def __init__(self, port=8000):
        self.listen(port)
        Application.__init__(self, **settings)

    @staticmethod
    def start():
        IOLoop.instance().start()


if __name__ == '__main__':
    HttpServer().start()

