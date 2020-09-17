#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from app.main.models.DemoAnimal import DemoAnimal


class DemoFish(DemoAnimal):

    def __init__(self, p_name):
        # super(DemoAnimal, self).__init__()
        DemoAnimal.__init__(self, p_name=p_name)
        pass

    def speak(self):
        DemoAnimal.speak(self)
        print('我用腮呼吸')

    # Fish类派生出swim功能
    # 派生：鱼有游泳的技能
    def swim(self):
        print('我会游泳')