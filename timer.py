from datetime import datetime
import time
import random


def timer_pause(a, b):
    for i in range(b):
        timer_A(a)


def timer_A(a):
    temp = random.random()
    ticktock(temp)
    time.sleep(a)


def timer_B(a, b):
    time.sleep(a)
    while True:
        temp = random.random()
        ticktock(temp)
        time.sleep(b)


def ticktock(n):
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    print('ticktock')
    print(n)
    pass


timer_pause(5, 5)
timer_B(30, 5)
