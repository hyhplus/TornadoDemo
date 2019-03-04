#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据流

- .write() 将数据写入输出缓冲区.
如果直接传入dict, 那Tornado会自动将其识别为json, 并把Content-Type设置为application/json,
如果你不想要这个Content-Type, 那么在.write()之后, 调用.set_header()重新设置就好了.
需要注意的是, 如果直接传入的是list, 考虑到安全问题(json数组会被认为是一段可执行的JavaScript脚本,
且<script src="*/secret.json">可以绕过跨站限制),list将不会被转换成json.

- .flush() 将输出缓冲区的数据写入socket.
如果设置了callback, 会在完成数据写入后回调. 需要注意的是, 同一时间只能有一个”等待”的flush callback,
如果”上一次”的flush callback还没执行, 又来了新的flush, 那么”上一次”的flush callback会被忽略掉.

- .finish() 完成响应，结束本次请求.
通常情况下, 请求会在return时自动调用.finish(), 只有在使用了异步装饰器@asynchronous或
其他将._auto_finish设置为False的操作, 才需要手动调用.finish().
"""

pass

