#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
options配置

全局配置：
tornado.options.define(
    name, default, type, multiple, help
)

命令行参数转换：
tornado.options.parse_command_line()

配置文件
#即在当前py文件目录创建config文件，并在py代码中加入以下代码，
tornado.options.parse_config_file("./config")
"""

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.options


# 定义变量
# 命令行访问：python elementary\demo3_options.py --port=8888
tornado.options.define(
    'port', default=8000, type=int, help='this is the port > for application'
)


class IndexHandler(RequestHandler):
    def get(self):
        self.write('我们既然改变不了规则，那就做到最好')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    tornado.options.parse_command_line()

    http_server = HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    # 启动IOLoop轮询监听
    IOLoop.current().start()




