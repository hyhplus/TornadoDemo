#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
application配置

程序调试之debug配置：
# 自动重启+取消缓存模板+取消缓存静态文件+提供追踪信息
tornado.web.Application([(...)], debug=True)
注：开发之初可以设置debug=True方便调试，开发完毕改为False.

路由信息初始化参数配置：
tornado.web.Application([(r'', Handler, {k: v})])
def initialize(self, k):
    pass

路由名称设置以及反解析
# 名称设置
tornado.web.Application([
    url(r'', handler, {k, v}, name='')
])
# 反解析操作
reverse_url(name)
"""
from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


class IndexHandler(RequestHandler):
    """
    主界面
    """
    def get(self):
        self.write("<a href='"+self.reverse_url('login')+"'>用户登录</a>")


class RegistHandler(RequestHandler):
    """
    注册模块
    """
    def initialize(self, title):
        self.title = title

    def get(self):
        self.write('注册业务处理：' + str(self.title))


class LoginHandler(RequestHandler):
    """
    登录模块
    """
    def get(self):
        self.write('用户登录页面展示')

    def post(self):
        self.write('用户登录功能处理')


if __name__ == '__main__':
    app = Application([
        (r'/', IndexHandler),
        (r'/register', RegistHandler, {'title': '会员注册'}),
        url(r'/login', LoginHandler, name='login'),
    ])

    http_server = HTTPServer(app)
    http_server.listen(8000)

    IOLoop.current().start()

