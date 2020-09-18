#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from app.main.models.DemoAnimal import DemoAnimal


class DemoSnake(DemoAnimal):
    def __init__(self):
        # super(DemoAnimal, self).__init__()
        pass

    def walk(self):
        DemoAnimal.walk(self)
        print("我会蠕动")

    def speak(self):
        DemoAnimal.speak(self)
        print('嘶嘶')

    # Snake类派生出venom功能
    # 派生：蛇有毒液的技能
    def venom(self):
        print('我有毒液')