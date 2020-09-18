# !/usr/bin/env python
# -*- encoding: utf-8 -*-

from app.main.models.DemoAnimal import DemoAnimal


class DemoCat(DemoAnimal):
    def __init__(self):
        # super(DemoAnimal, self).__init__()
        pass

    def walk(self):
        DemoAnimal.walk(self)
        print("我会跑")

    def speak(self, blood):
        DemoAnimal.speak(self)
        print('喵喵 my blood is {}'.format(blood))

    # Cat类派生出catch_mouse功能
    # 派生：猫有抓老鼠的技能
    def catch_mouse(self):
        print('我会抓老鼠')


