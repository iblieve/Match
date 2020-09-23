#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading


class XSingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with XSingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(XSingletonType, cls).__call__(*args, **kwargs)
        return cls._instance
