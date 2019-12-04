#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop


# 设置 user_agent 请求列表, 通过访问请求头信息进行反爬虫
user_agent = ['Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
              'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
              ]


class AccessHandler(tornado.web.RequestHandler):
    def get(self):
        user_agent_i = self.request.headers['User-Agent']
        print(user_agent_i)
        if user_agent_i not in user_agent:
            self.send_error(403)
        else:
            self.write('Hello Tornado!')


# 设置 ip 计数, 测试用户访问次数是否正常
ip_count = {}


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # 获取客户端的 ip 地址
        ip = self.request.remote_ip

        # 每次访问 ip 加 1
        num = ip_count.get(ip, 0) + 1
        # 将访问次数存放在字典中
        ip_count[ip] = num

        if ip_count[ip] > 5:
            self.send_error(403)
            print(ip_count)
        else:
            self.write('Hello Admin! 12345')


def main():
    app = tornado.web.Application([
        (r'^/$', AccessHandler),
        (r'^/login/$', LoginHandler)
    ])

    app.listen(8888, '192.168.31.215')

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
