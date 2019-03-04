#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
writerror

- .send_error() 用于发送HTTP错误页（状态码）。该操作会调用.clear() .set_status()
- .write_error() 用于清除headers, 设置状态码，发送错误页。重写.write_error()可以自定义错误页
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):

    def get(self):
        self.write("hello baidu.com")
        self.send_error(404, msg='页面丢失', info='家里服务器搞对象了')

    def write_error(self, status_code, **kwargs):
        self.write('<h1>出错啦，工程师MM正在赶来的途中...</h1>')
        self.write('<p>错误信息：%s</p>' % kwargs['msg'])
        self.write('<p>错误描述：%s</p>' % kwargs['info'])


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8000)

    IOLoop.current().start()

