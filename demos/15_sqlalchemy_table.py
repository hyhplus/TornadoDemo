#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/10 9:53
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
        return '[User:{0}, {1}'.format(self.id, self.account)


class Address(Base):
    __tablename__ = 't_addr'

    id = Column(Int, primary_key=True, autoincrement=True)
    aname = Column(String(30), unique=True)


from sqlalchemy.orm import sessionmaker
import datetime


def insertUser(account, pwd):
    # 创建连接池
    conn_pool = sessionmaker(bind=engine)

    # 获取一个连接
    conn = conn_pool()

    # 创建 User 对象
    user = User(account=account, pwd=pwd, birth=datetime.date(2000, 12, 23))

    # 插入到表中
    conn.add(user)

    # 提交事务
    conn.commit()

    # 刷新
    conn.refresh(user)

    # 断开连接
    conn.close()

    return user


# insertUser('Alan121', '666')  # 注意字段的唯一属性


def insert_many(users: []):
    conn_pool = sessionmaker(bind=engine)
    conn = conn_pool()
    conn.add_all(users)
    conn.commit()
    [conn.refresh(u) for u in users]
    conn.close()

    return users


user1 = User(account='GeHu2', birth=datetime.date(1978, 12, 12))
user2 = User(account='JinHu2', birth=datetime.date(1998, 2, 28))
user3 = User(account='LaiHu2', birth=datetime.date(1988, 8, 31))
add_ = Address(aname='beijing')

user_lst = [user2, user3, add_]
insert_many(user_lst)


