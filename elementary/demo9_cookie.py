#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):

    def get(self):
        self.write('hello google.com')
        self.set_cookie('username', 'admin')
        print(self.get_cookie('username'))   # 第一次是None; 后面是admin
        print(self.cookies)


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8000)

    IOLoop.current().start()





