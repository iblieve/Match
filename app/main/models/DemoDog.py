#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from app.main.models.DemoAnimal import DemoAnimal


class DemoDog(DemoAnimal):
    def __init__(self):
        # super(DemoAnimal, self).__init__()
        pass

    def walk(self):
        DemoAnimal.walk(self)
        print("我会跑")

    def speak(self):
        DemoAnimal.speak(self)
        print('汪汪')

    # Dog类派生出bite功能
    # 派生：狗有咬人的技能
    def bite(self):
        print('我会咬人')
