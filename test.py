#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, datetime
import xlrd, xlwt

from app.utils.XUtils import XUtils
from app.main.models.DemoAnimal import DemoAnimal
from app.main.models.DemoCat import DemoCat
from app.main.models.DemoDog import DemoDog


def main(p_argv):
    cat = DemoCat(p_name='加菲', p_blood='AB')
    cat.catch_mouse()
    cat.speak()
    cat.walk()
    
    print('\n')

    dog = DemoDog(p_name='旺财')
    dog.bite()
    dog.speak()
    dog.walk()

    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
