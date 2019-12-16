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
        return '[User:{0}, {1}]'.format(self.id, self.account)


class Address(Base):
    __tablename__ = 't_addr'

    id = Column(Int, primary_key=True, autoincrement=True)
    aname = Column(String(30), unique=True)


from sqlalchemy.orm import sessionmaker


# 查询
def query_all(clsname):
    conn_pool = sessionmaker(bind=engine)
    conn = conn_pool()

    # 执行查询操作
    users = conn.query(clsname).all()

    conn.close()
    return users


# print(query_all(User))


# 排序
def order_by_user(cls):
    conn_pool = sessionmaker(bind=engine)
    conn = conn_pool()

    users = conn.query(cls).order_by(cls.id.desc()).all()
    conn.close()
    return users


# print(order_by_user(User))


# 获取记录数
def count(cls):
    conn_pool = sessionmaker(bind=engine)
    conn = conn_pool()

    c = conn.query(cls).count()
    conn.close()
    return c


# print(count(Address))


# 分页
def page(cls, num, size=2):
    """
    param cls: 对象类名
    param num: 当前页
    param size: 一页的记录数
    return:
    """

    conn_pool = sessionmaker(bind=engine)
    conn = conn_pool()

    data = conn.query(cls).offset((num-1)*size).limit(size).all()
    conn.close()
    return data


# print(page(User, 2))


# 通过主键查询记录
def query_by_pk(cls, pk):
    conn_pool = sessionmaker(bind=engine)
    conn = conn_pool()
    data = conn.query(cls).get(pk)
    conn.close()
    return data


# print(query_by_pk(User, 6))


# 将公共部分提取成装饰器
def wrapper_session(func):
    def _wrapper(*args, **kwargs):
        from sqlalchemy.orm.session import sessionmaker
        conn_pool = sessionmaker(bind=engine)
        conn = conn_pool()
        data = func(conn, *args, **kwargs)
        conn.close()
        return data
    return _wrapper


# 通过某个字段删除一条记录
@wrapper_session
def delete_by_column(conn, cls, id):
    conn.query(cls).filter(cls.id == id).delete()
    conn.commit()


# delete_by_column(cls=User, id=6)


# 通过对象来更新属性
@wrapper_session
def update_user_by_attr(conn, obj):
    conn.add(obj)
    conn.commit()


# u = query_by_pk(User, 7)
# u.pwd = "user_7's pwd"
# update_user_by_attr(obj=u)


# filter(单条件查询)
@wrapper_session
def filter_single(conn, account):
    u = conn.query(User).filter(User.account == account).all()
    return u


# print(filter_single('LaiHu'))


# filter(多条件查询)(与的关系)
@wrapper_session
def filter_and(conn, account, pwd):
    from sqlalchemy import and_
    us = conn.query(User).filter(and_(User.account == account, User.pwd == pwd)).all()
    # us = conn.query(User).filter(User.account == account, User.pwd == pwd).all()
    return us


# print(filter_and('Alan', '666'))


# filter(多条件查询)(或的关系)
@wrapper_session
def filter_or(conn, account, pwd):
    from sqlalchemy import or_
    u = conn.query(User).filter(or_(User.account == account, User.pwd == pwd)).all()
    return u


# print(filter_or('Alan', 666))


# filter()(非的关系)
@wrapper_session
def filter_not(conn, account):
    from sqlalchemy import not_
    data = conn.query(User).filter(not_(User.account == account)).all()
    return data


# print(filter_not('Alan'))


# filter(多条件查询)(嵌套使用)
@wrapper_session
def filter_nesting(conn, account, pwd):
    from sqlalchemy import not_, or_
    user = conn.query(User).filter(not_(or_(User.account == account, User.pwd == pwd))).all()
    return user


# print(filter_nesting('Alan', '666'))


# 分组查询
@wrapper_session
def group_by_query(conn):
    from sqlalchemy.sql.functions import func
    data = conn.query(func.count(User.id), User.pwd).group_by(User.pwd).all()
    return data


# print(group_by_query())
# [(1, '126'), (1, '127'), (5, '666'), (1, "user_7's pwd")]


# 查看部分字段的值
@wrapper_session
def query_part(conn):
    data = conn.query(User.id.label('编号'), User.account.label('用户名')).all()
    return data


# print(query_part())












