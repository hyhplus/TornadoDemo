#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: Evan
@time: 2019/12/4 15:16
"""

import tornado.web
import tornado.ioloop


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        """
        cookie 在 Response Headers
        Set-Cookie: hello="2|1:0|10:1575445821|5:hello|8:RXZhbg==|c6eb04740d9320d33053b28cb0ea8a799f17b26950869fe22309671ccec57513"; expires=Fri, 03 Jan 2020 07:50:21 GMT; Path=/
        :return:
        """
        # self.set_cookie('username', 'admin', expires_days=3)
        self.set_secure_cookie('hello', 'Evan')


class GetCookieHandler(tornado.web.RequestHandler):
    def get(self):
        """
        cookie 在 Request Headers
        Cookie: hello="2|1:0|10:1575445307|5:hello|8:RXZhbg==|b062aa734378e7a3177e8626d66acee4b52b4dc4df1293c20eb926d25824607e"
        """
        # username = self.get_cookie('username')

        username = self.get_secure_cookie('hello')
        self.write(username)


settings = {
    'cookie_secret': 'asd123fgh'
}

app = tornado.web.Application([
    (r'^/$', CookieHandler),
    (r'^/getCookie/$', GetCookieHandler)
], **settings)

app.listen(8000)

tornado.ioloop.IOLoop.instance().start()


