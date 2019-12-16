#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/12 10:10
"""

import os
from abc import ABC
from typing import Union

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.websocket import WebSocketHandler


class IndexHandler(RequestHandler, ABC):
    def get(self):
        self.render('index.html')


class SocketHandler(WebSocketHandler, ABC):
    def open(self, *args: str, **kwargs: str):
        print('开启服务器连接')
        self.write_message('send msg')

    def on_message(self, message: Union[str, bytes]):
        print('收到客户端的消息：{}'.format(message))
        self.write_message('hello client!')

    def on_close(self):
        print('断开连接！')

    def check_origin(self, origin: str):
        return True


app = Application([
    (r'^/$', IndexHandler),
    (r'^/socket/$', SocketHandler),
], template_path=os.path.join(os.getcwd(), 'templates'))


app.listen(8888)

IOLoop.current().start()






