#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/3 16:31

use `pip install mysqlclient` to install MySQLdb
"""
import tornado.web
import tornado.ioloop
import MySQLdb
"""
    :param str host:        host to connect
    :param str user:        user to connect as
    :param str password:    password to use
    :param str passwd:      alias of password, for backward compatibility
    :param str database:    database to use
    :param str db:          alias of database, for backward compatibility
    :param int port:        TCP/IP port to connect to
    :param str unix_socket: location of unix_socket to use
    :param dict conv:       conversion dictionary, see MySQLdb.converters
    :param int connect_timeout:
    ...
"""


def _get_connect():
    return MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='123456',
        db='tornado_20191203',
        port=3306
    )


class RegisterHandler(tornado.web.RequestHandler):

    def initialize(self, connect):
        self.connect = connect

    def get(self):
        self.render('templates/register.html')

    def post(self):
        # 获取请求参数
        username = self.get_body_argument('account')
        password = self.get_body_argument('password')

        # 将数据插入到数据库中
        try:
            cursor = self.connect.cursor()
            # MySQL获取系统当前时间函数：sysdate() / now()
            cursor.execute('insert into t_user values(null, "{0}", "{1}", sysdate())'.format(username, password))
            self.connect.commit()
            self.write('注册成功！')
        except Exception as ret:
            print(ret)
            self.connect.rollback()
            self.redirect('/register/')


def main():
    app = tornado.web.Application([
        (r'^/register/$', RegisterHandler, {'connect': _get_connect()}),
    ])

    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
