#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop


# 处理类
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/login.html')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        account = self.get_query_argument('account')
        password = self.get_query_argument('password')
        self.write(account+', '+password)

    def post(self):
        account = self.get_body_argument('account')
        password = self.get_body_argument('password')
        print(account, password)

        img1 = self.request.files['img']
        print(img1)

        content = None
        filename = None
        content_type = None

        for img in self.request.files['img']:
            content = img['body']
            filename = img['filename']
            content_type = img['content_type']

        import os
        dirs = os.path.join(os.getcwd(), 'files', filename)

        with open(dirs, 'wb') as fw:
            fw.write(content)

        # 显示图片到浏览器界面中
        # 设置响应头信息
        self.set_header('Content-Type', content_type)
        self.write(content)

        # self.redirect('http://www.baidu.com/')


# 设置路由
app = tornado.web.Application([
    (r'^/$', IndexHandler),
    (r'^/login/$', LoginHandler)
])

# 绑定端口号
app.listen(8888)

# 启动连接
tornado.ioloop.IOLoop.current().start()
