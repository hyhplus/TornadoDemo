#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/6 9:54
@description: torndb tables reference: t_student, t_cls, t_course
"""
import torndb

conn = torndb.Connection(
    host='127.0.0.1',
    database='tornado_20191203',
    user='root',
    password='123456',
    time_zone="+8:00"  # 设置时区，不然有8小时的时差
)


def insert(cls_name, stu_name, course_names: []):

    # 插入班级表数据
    cls_lst = conn.query('select cno from t_cls where cname="{0}"'.format(cls_name))
    if cls_lst:
        clsid = cls_lst[0]['cno']
    else:
        clsid = conn.insert('insert into t_cls values(null, "{0}")'.format(cls_name))

    # 插入学生表数据
    stu_lst = conn.query('select sno from t_student where sname="{0}"'.format(stu_name))
    if stu_lst:
        sno = stu_lst[0]['sno']
    else:
        sno = conn.insert('insert into t_student values(null, "{0}", "{1}")'.format(stu_name, clsid))

    # 插入课程表数据
    courseid_lst = []
    for cn in course_names:
        course_lst = conn.query('select courseid from t_course where coursename="{0}"'.format(cn))
        if course_lst:
            courseid_lst.append(course_lst[0]['courseid'])
        else:
            cid = conn.insert('insert into t_course values(null, "{}")'.format(cn))
            courseid_lst.append(cid)

    # 插入中间表
    for courseid in courseid_lst:
        conn.insert('insert into t_sc values(null, "{0}", "{1}")'.format(sno, courseid))

    # 关闭数据库连接
    conn.close()


insert('Python3.7x', 'TomWong', ['Python', 'Tornado'])
