#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/4 10:28
"""
# 重定向的几种方式，以及底层实现原理

import tornado.web
import tornado.ioloop
from tornado.routing import URLSpec


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 302重定向
        # self.redirect('http://www.baidu.com')

        self.set_status(301)
        self.set_header('Location', 'http://baidu.com')


class ReverseHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect(self.reverse_url('index'))


def main():
    app = tornado.web.Application([
        (r'^/$', IndexHandler),
        (r'^/red/$', tornado.web.RedirectHandler, {'url': 'https://www.taobao.com'}),
        URLSpec(r'^/fix$', IndexHandler, name='index'),
        (r'^/reverse/$', ReverseHandler),
    ])

    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()


