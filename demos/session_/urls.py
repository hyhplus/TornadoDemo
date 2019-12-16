#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: v1.0
@author: Evan
@time: 2019/12/11 9:33
"""
from .views import CenterHandler, LoginHandler
import os


settings = {
    'handlers': [
        (r'^/login/$', LoginHandler),
        (r'^/center/$', CenterHandler)
    ], 'template_path': os.path.join(os.getcwd(), 'templates')
}
