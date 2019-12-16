#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/16 14:14
"""

import os
import datetime

from abc import ABC
from typing import Union

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.websocket import WebSocketHandler


class IndexHandler(RequestHandler, ABC):
    def get(self):
        self.render('chat.html')


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


user_lst = set()


class ChatHandler(WebSocketHandler, ABC):
    def open(self, *args: str, **kwargs: str):
        user_lst.add(self)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        [user.write_message('{}-{}:上线啦！'.format(self.request.remote_ip, now)) for user in user_lst]

    def on_message(self, message: Union[str, bytes]):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        [user.write_message('{}-{}说:{}'.format(self.request.remote_ip, now, message)) for user in user_lst]

    def on_close(self):
        user_lst.remove(self)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        [user.write_message('{}-{}:下线了~'.format(self.request.remote_ip, now)) for user in user_lst]


app = Application([
    (r'^/$', IndexHandler),
    (r'^/socket/$', SocketHandler),
    (r'^/chat/$', ChatHandler),
], template_path=os.path.join(os.getcwd(), 'templates'))


app.listen(8888, address='192.168.31.213')

IOLoop.current().start()
