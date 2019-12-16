#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/6 10:33
"""
import win32api
import win32con


class AutoRun(object):
    def __init__(self):
        name = 'MySQL服务器'  # 要添加的项值名称
        path = 'D:\\mysql5.7\\bin\\mysqld.exe'  # 要添加的exe路径
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
            win32api.RegCloseKey(key)
        except:
            print('添加失败')
        print('添加成功！')


if __name__ == '__main__':
    auto = AutoRun()
