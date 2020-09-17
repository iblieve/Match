#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class DemoAnimal:
    name = None

    def __init__(self, p_name):
        self.name = p_name

    def speak(self):
        pass

    def walk(self):
        """
        该方法会被其所有子类继承, 子类无需实现该函数即可调用到父类的walk方法
        :return:
        """
        print('我会走')
