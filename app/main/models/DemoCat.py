# !/usr/bin/env python
# -*- encoding: utf-8 -*-

from app.main.models.DemoAnimal import DemoAnimal


class DemoCat(DemoAnimal):

    blood = None

    def __init__(self, p_name=None, p_blood=None):
        # super(DemoAnimal, self).__init__()
        DemoAnimal.__init__(self, p_name=p_name)
        self.blood = p_blood
        pass

    def speak(self):
        DemoAnimal.speak(self)
        print('喵喵 my blood is {}'.format(self.blood))

    # Cat类派生出catch_mouse功能
    # 派生：猫有抓老鼠的技能
    def catch_mouse(self):
        print('我会抓老鼠')
