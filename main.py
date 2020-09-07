#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, datetime


def main(p_argv):
    print("hello world")

    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
