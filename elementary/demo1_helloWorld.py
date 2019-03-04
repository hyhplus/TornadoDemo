#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/xc_zhou/article/details/80637714

tornado.web: tornado的基础web框架
    - RequestHandler: 封装对请求处理的所有信息和处理方法
    - get/post/..: 封装对应的请求方法
    - write(): 封装响应信息，写响应信息的一个方法

tornado.ioloop: 核心io循环模块，封装Linux的epoll和BSD的kqueue,
tornado高性能处理的核心
    - current(): 返回当前线程的IOLoop实例对象
    - start(): 启动IOLoop实例对象的IO循环，开启监听
"""
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """
    定义处理类型
    """
    def get(self):
        """
        添加一个处理get请求方式的方法
        访问地址：http://localhost:8888/
        :return:
        """
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')


if __name__ == '__main__':
    # 创建一个应用对象
    app = tornado.web.Application([(r'/', IndexHandler)])
    # 绑定一个监听端口
    app.listen(8888)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()

