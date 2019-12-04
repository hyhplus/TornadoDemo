#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/4 14:11
"""

import tornado.web
import tornado.ioloop
import MySQLdb


class LoginHandler(tornado.web.RequestHandler):
    def initialize(self, conn):
        self.conn = conn

    def prepare(self):
        print('prepare')
        if self.request.method == 'POST':
            # 获取请求参数
            self.username = self.get_body_argument('account')
            self.password = self.get_body_argument('password')

    def get(self):
        self.render('templates/login.html')

    def post(self):
        print('POST request')
        cursor = self.conn.cursor()
        cursor.execute('select * from t_user where username="{0}" and password="{1}"'.format(self.username, self.password))
        user = cursor.fetchone()

        if user:
            self.write('登录成功！')
        else:
            self.write('登录失败！')

    def write_error(self, status_code: int, **kwargs):
        self.render('templates/error.html')

    def set_default_headers(self):
        self.set_header('Server', 'SSServer/1.0')


def main():
    settings = {'debug': True}
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'passwd': '123456',
        'db': 'tornado_20191203',
        'port': 3306
    }
    app = tornado.web.Application([
        (r'^/login/$', LoginHandler, {'conn': MySQLdb.connect(**db_config)})
    ], **settings)

    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()



