#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 15:51
"""
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPClient
from tornado.ioloop import IOLoop


def parse(content):
    import bs4
    bs = bs4.BeautifulSoup(content, 'html.parser')
    text = [a.text for a in bs.select('ul.foot_nav.main a')]
    for a in text:
        print(a)


def handle_response(response):
    body = response.body

    import os
    base_dir = os.path.join(os.getcwd(), 'templates')
    file = os.path.join(base_dir, 'index_asy.html')

    with open(file, 'wb') as fw:
        fw.write(body)

    parse(body)


def load(url, callback):
    http_client = AsyncHTTPClient()
    response = http_client.fetch(url, callback=callback)

    print(response)
    return response


req = HTTPRequest(url='http://www.bjsxt.com', method='POST', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}, body='name=heiGe')
load('http://www.bjsxt.com', handle_response)

IOLoop.instance().start()
