#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class DemoAnimal(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def walk(self):
        """
        该方法会被其所有子类继承, 子类无需实现该函数即可调用到父类的walk方法
        :return:
        """
        # print('我会走')
        pass


