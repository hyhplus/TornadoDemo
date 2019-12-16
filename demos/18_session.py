#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/10 17:35

@description: tornado 自定义session
"""
import uuid
import pickle


class Session(object):
    def __init__(self):
        self.__sessionid = uuid.uuid4().get_hex()
        self.cache = {}

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key, default=None):
        return self.cache.get(key, default)

    def clear(self):
        self.cache.clear()

    @property
    def sessionid(self):
        return self.__sessionid

    # 序列化session对象
    def serialization(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialization(string):
        return pickle.loads(string)


class SessionManager(object):
    import redis
    conn = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

    @classmethod
    def cache2redis(cls, session):
        cls.conn.set(session.sessionid, session.serialization(), ex=14*24*60*60)

    @classmethod
    def getSessionByid(cls, sessionid):
        rs = Session.deserialization(cls.conn.get(sessionid)) if cls.conn.get(sessionid) else None

        if not rs:
            rs = Session()

        return rs
