from datetime import datetime
from threading import Timer
import time
import random


def timer_A_pause(a):
    timer_A()
    time.sleep(a)
    timer.cancel()


def timer_A():
    temp = random.random()
    ticktock(temp)
    global timer
    timer = Timer(5, timer_A)
    timer.start()


def timer_B():
    # timer = Timer(60, timer_B)
    # timer.start()
    # print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    # print("123")
    # timer_A()
    time.sleep(30)
    timer_A()


def ticktock(n):
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    print('ticktock')
    print(n)


timer_A_pause(30)
timer_B()
