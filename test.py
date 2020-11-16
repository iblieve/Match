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

from Stack import Stack


def main(p_argv=None):
    stack = Stack[int]()
    stack.push(2)
    item = stack.pop()
    print(item)
    stack.push('x')  # Type error
    item = stack.pop()
    print(item)

    print('\n')

    stack = Stack[DemoFish]()
    stack.push(DemoFish())
    item = stack.pop()
    item.speak()

    print('\n')

    stack = Stack[DemoDog]()
    stack.push(DemoDog())
    item = stack.pop()
    item.speak()

    print('\n')

    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
