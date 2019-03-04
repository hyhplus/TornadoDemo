#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
httpserver底层处理
httpserver监听端口：
tornado.httpserver.HTTPServer(app)
httpserver.listen(port)

httpserver实现多进程操作:
tornado.httpserver.HTTPServer(app)
httpserver.bind(port)
httpserver.start(0/None/<0/num)
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class IndexHandler(RequestHandler):
    def get(self):
        """
        访问地址：http://localhost:8888/
        :return:
        """
        self.write('给自己一点时间，清理所有的荒唐与期望。')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    http_server = HTTPServer(app)
    # 最原始的方式
    http_server.bind(8888)
    http_server.start(1)

    # 启动IOLoop轮询监听
    IOLoop.current().start()





