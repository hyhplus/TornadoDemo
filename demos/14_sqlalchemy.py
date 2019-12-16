#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/9 17:53
"""
# 1. 安装sqlalchemy模块
"""
pip install sqlalchemy
"""

# 2. 配置引擎
from sqlalchemy.engine import create_engine
conn_url = 'mysql://root:123456@127.0.0.1:3306/tornado_20191203?charset=utf8'
engine = create_engine(conn_url, encoding='utf-8', echo=True)

# 3. 声明 ORM 基类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

# 4. 创建列和字段类型
from sqlalchemy import Column
from sqlalchemy.types import Integer as Int, String, Date, DateTime, Float, Text


# 5. 创建 ORM 类
class User(Base):
    __tablename__ = 't_cuser'

    id = Column(Int, primary_key=True, autoincrement=True)
    account = Column(String(length=20), unique=True)
    pwd = Column(String(length=20))
    birth = Column(Date)
    score = Column(Float(decimal_return_scale=2))

    def __repr__(self):
        return '[User:{0}, {1}]'.format(self.id, self.account)


class Address(Base):
    __tablename__ = 't_addr'

    id = Column(Int, primary_key=True, autoincrement=True)
    aname = Column(String(30), unique=True)


# 6. 如果表已经存在，则不执行当前存在表的创建操作
Base.metadata.create_all()

# 7. 利用基类删除所有的数据库表
# Base.metadata.drop_all()
