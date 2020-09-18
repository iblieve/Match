#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, datetime
import xlrd, xlwt

from app.utils.XUtils import XUtils
from app.main.models.DemoAnimal import DemoAnimal
from app.main.models.DemoCat import DemoCat
from app.main.models.DemoDog import DemoDog
from app.main.models.DemoFish import DemoFish
from app.main.models.DemoSnake import DemoSnake


def speak(obj,blood):
    obj.speak(blood)


def main(p_argv):
    cat = DemoCat()
    cat.catch_mouse()
    speak(cat, "AB")
    cat.walk()
    
    print('\n')

    dog = DemoDog()
    dog.bite()
    dog.speak()
    dog.walk()

    print('\n')

    fish = DemoFish()
    fish.swim()
    fish.speak()
    fish.walk()

    print('\n')

    snake = DemoSnake()
    snake.venom()
    snake.speak()
    snake.walk()

    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
