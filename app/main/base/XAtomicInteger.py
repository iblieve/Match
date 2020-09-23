#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading


class XAtomicInteger(object):
    _value = None
    _lock = None

    def __init__(self, p_value=0):
        """
        Creates a new XAtomicInteger with the given initial value.
        :param p_value:
        """
        self._value = p_value
        self._lock = threading.Lock()

    def increment_and_get(self) -> (int):
        """
        Atomically increments by one the current value.
        :return:
        """
        with self._lock:
            self._value += 1
            return self._value

    def decrement_and_get(self) -> (int):
        """
        Atomically decrements by one the current value.
        :return:
        """
        with self._lock:
            self._value -= 1
            return self._value

    def get(self) -> (int):
        """
        Gets the current value.
        :return:
        """
        with self._lock:
            return self._value

    def set(self, p_new_value: int = 0) -> (int):
        """
        Sets to the given value.
        :param p_new_value:
        :return:
        """
        with self._lock:
            self._value = p_new_value
            return self._value
