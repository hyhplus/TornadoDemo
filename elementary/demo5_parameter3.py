#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
其他参数

通过request获取参数数据
method/host/uri/path/query/version/headers/body/remote_ip/files
"""
import json

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        print(self.request)

        json_str = {'username': 'admin', 'password': '123456'}
        self.write(json.dumps(json_str))


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8000)
    IOLoop.current().start()


