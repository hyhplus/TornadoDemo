#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 9:32
"""
from abc import ABC
from typing import Any, Union

from tornado.web import RequestHandler

from utils.session_t import SessionManager, Session
from .models import User


class BaseHandler(RequestHandler, ABC):

    session: Union[Session, Any]

    def prepare(self):
        # 从 cookie 中获取 session_id
        c_session_id = self.get_cookie('sessionid', '')

        # 根据 session_id 获取 session 对象
        session = SessionManager.getSessionByid(c_session_id)

        # 判断是否需要重置 cookie 中的 session_id
        if c_session_id != session.sessionid:
            self.set_cookie('sessionid', session.sessionid, expires_days=14)

        self.session = session

    def on_finish(self):
        SessionManager.cache2redis(self.session)


class LoginHandler(BaseHandler, ABC):
    def get(self):
        self.render('login.html')

    def post(self):
        # 获取请求参数
        account = self.get_argument('account', '')
        password = self.get_argument('password', '')
        user = User(account, password)

        # 判断是否登录成功
        if account == 'admin' and password == '123':

            # 将登录用户对象存放至 session 对象中
            self.session.set('user', user)
            self.redirect('/center/')


class CenterHandler(BaseHandler, ABC):
    def get(self):
        # 从 session 中获取当前登录用户对象
        user = self.session.get('user')
        self.write('欢迎{}登录成功！'.format(user.account))


