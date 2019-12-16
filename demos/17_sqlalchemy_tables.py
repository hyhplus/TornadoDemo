#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/10 16:05
"""
import datetime

from sqlalchemy.engine import create_engine
conn_url = 'mysql://root:123456@127.0.0.1:3306/tornado_20191203?charset=utf8'
engine = create_engine(conn_url, encoding='utf-8', echo=True)

# 声明 ORM 基类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

# 创建列和字段类型
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, DateTime, Float, Text


# 建表
# 班级表 t_cls
# 学生表 t_student
# 课程表 t_course
# 关联表 t_sc
class Clazz(Base):
    __tablename__ = 't_cls'

    cno = Column(Integer, primary_key=True, autoincrement=True)
    cname = Column(String(length=30), unique=True, nullable=False)

    def __repr__(self):
        return '<Clazz:{},{}>'.format(self.cno, self.cname)


class Student(Base):
    __tablename__ = 't_student'

    sno = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(length=30), unique=True, nullable=False)
    score = Column(Float(decimal_return_scale=2), default=10.00)
    birth = Column(Date, default=datetime.date.today())
    description = Column(Text, nullable=True)
    cno = Column(Integer, ForeignKey(Clazz.cno, ondelete='CASCADE', onupdate='CASCADE'))

    def __repr__(self):
        return '<Student:{},{},{}>'.format(self.sno, self.sname, self.cno)


class Course(Base):
    __tablename__ = 't_course'

    courseid = Column(Integer, primary_key=True, autoincrement=True)
    coursename = Column(String(length=30), unique=True, nullable=False)

    def __repr__(self):
        return '<Course:{},{}>'.format(self.courseid, self.coursename)


class SC(Base):
    __tablename__ = 't_sc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sno = Column(Integer, ForeignKey(Student.sno, ondelete='CASCADE', onupdate='CASCADE'))
    courseid = Column(Integer, ForeignKey(Course.courseid, ondelete='CASCADE', onupdate='CASCADE'))

    def __repr__(self):
        return '<SC:{},{}>'.format(self.sno, self.courseid)


# 6. 如果表已经存在，则不执行当前存在表的创建操作
# Base.metadata.create_all()

# Base.metadata.drop_all()


# 插入多表操作
def insert_many(cname, sname, coursenames: []):
    from sqlalchemy.orm import sessionmaker
    conn_pool = sessionmaker()
    conn = conn_pool()

    # 1. 插入班级表
    cls_lst = conn.query(Clazz.cno).filter(Clazz.cname == cname).all()

    if cls_lst:
        cno = cls_lst[0].cno
    else:
        cls = Clazz(cname=cname)
        conn.add(cls)
        conn.commit()
        conn.refresh(cls)
        cno = cls.cno

    # 2. 插入学生表
    stu_lst = conn.query(Student.sno).filter(Student.sname == sname).all()

    if stu_lst:
        sno = stu_lst[0].sno
    else:
        stu = Student(sname=sname, cno=cno)
        conn.add(stu)
        conn.commit()
        conn.refresh(stu)
        sno = stu.sno

    # 3. 插入课程表
    courseid_lst = []
    for cn in coursenames:
        course_lst = conn.query(Course.courseid).filter(Course.coursename == cn).all()

        if course_lst:
            courseid_lst.append(courseid_lst[0].courseid)
        else:
            course = Course(coursename=cn)
            conn.add(course)
            conn.commit()
            conn.refresh(course)
            courseid_lst.append(course.courseid)
    # 4. 插入中间表
    for cid in courseid_lst:
        sc = SC(sno=sno, courseid=cid)
        conn.add(sc)
        conn.commit()
        conn.refresh(sc)

    conn.close()


insert_many('Python3.7', 'TomHu', ['HTML', 'JavaScript'])


