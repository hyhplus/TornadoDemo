#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/5 14:23
"""
import torndb

conn = torndb.Connection(
    host='127.0.0.1',
    database='tornado_20191203',
    user='root',
    password='123456',
    time_zone="+8:00"  # 设置时区，不然有8小时的时差
)


# 插入单条记录
def insert_user(u_name, pwd):

    row_id = conn.insert('insert into t_user values(null,"{0}","{1}",sysdate())'.format(u_name, pwd))
    print(row_id)

    conn.close()


insert_user('Evan@qq.com', '123456')

# 修改 torndb 源码支持 Python3.x
# E:\hyh_doc\Enev\TornadoDemo\Lib\site-packages\torndb.py 260行改为list append()
"""
if MySQLdb is not None:
    # Fix the access conversions to properly recognize unicode/binary
    FIELD_TYPE = MySQLdb.constants.FIELD_TYPE
    FLAG = MySQLdb.constants.FLAG
    CONVERSIONS = copy.copy(MySQLdb.converters.conversions)

    field_types = [FIELD_TYPE.BLOB, FIELD_TYPE.STRING, FIELD_TYPE.VAR_STRING]
    if 'VARCHAR' in vars(FIELD_TYPE):
        field_types.append(FIELD_TYPE.VARCHAR)

    for field_type in field_types:
        # CONVERSIONS[field_type] = [(FLAG.BINARY, str)] + CONVERSIONS[field_type]
        CONVERSIONS[field_type] = [(FLAG.BINARY, str)].append(CONVERSIONS[field_type])

    # Alias some common MySQL exceptions
    IntegrityError = MySQLdb.IntegrityError
    OperationalError = MySQLdb.OperationalError
"""

# 设置连接超时时间为10s
"""
class Connection(object):
    def __init__(self, host, database, user=None, password=None,
                 max_idle_time=7 * 3600, connect_timeout=10, 
                 time_zone="+0:00", charset = "utf8", sql_mode="TRADITIONAL"):
"""


# 增加多条记录
def insert_many(args: list):
    sql = 'insert into t_user values(null, %s, %s, now())'
    rowid = conn.insertmany(sql, args)
    print(rowid)
    conn.close()


# insert_many([('zhanghua', '666'), ('Tom', '333')])


# 查询
def query():
    sql = 'select * from t_user'
    users = conn.query(sql)
    print(users)
    conn.close()


# query()
"""
izip --> zip_longest

    def query(self, query, *parameters, **kwparameters):
        ''''''
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters, kwparameters)
            column_names = [d[0] for d in cursor.description]
            return [Row(itertools.zip_longest(column_names, row)) for row in cursor]
        finally:
            cursor.close()
"""


# 条件查询
def query_sort(username):
    sql = 'select * from t_user where username="{}"'.format(username)
    # 模糊查询
    sql1 = 'select * from t_user where username like "{name}%%"'.format(name=username)

    users = conn.query(sql1)
    print(users)

    conn.close()


# query_sort('')


# 排序
def sort_order_by(rule):
    order = 'ASC'
    if rule.startswith('-'):
        order = 'DESC'
        rule = rule[1:]

    sql = 'select * from t_user order by {} {}'.format(rule, order)
    users = conn.query(sql)
    conn.close()

    return users


# print(sort_order_by('-userid'))


# 分页
def query_all_page(num, size=2):
    """
    :param num:   第几页
    :param size:  一页显示多少条记录
    """
    sql = 'select * from t_user limit {page},{size}'.format(page=(num-1)*size, size=size)
    users = conn.query(sql)
    print(users)
    conn.close()


# query_all_page(4)


# 更新
def update(username, new_pwd):
    sql = 'update t_user set password="{pwd}" where username="{username}"'.format(username=username, pwd=new_pwd)
    rowid = conn.update(sql)
    conn.close()

    return rowid


# print(update('admin', '123456'))


# 删除
def delete(username):
    sql = 'delete from t_user where username="{username}"'.format(username=username)
    conn.execute(sql)
    conn.close()


# delete('Evan@qq.com')


