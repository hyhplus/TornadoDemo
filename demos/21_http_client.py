#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 14:51
"""
"""
同步请求
"""
from tornado.httpclient import HTTPClient, HTTPRequest


# 发送 GET 同步请求
def get_request(url):
    httpclient = HTTPClient()
    response = httpclient.fetch(url)
    return response.body


# print(get_request('http://www.bjsxt.com'))


# 发送 POST 同步请求
def post_(request):
    http_client = HTTPClient()
    response = http_client.fetch(request)
    return response.body.decode('utf-8')


req = HTTPRequest(url='http://www.jd.com', method='POST', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}, body='name=heiGe')
print(post_(req))



