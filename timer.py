from datetime import datetime
import time
import random


# 每n秒执行一次
def timer(n):
    while True:
        temp = random.random()
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        time.sleep(n)
        ticktock(temp)


def ticktock(n):
    print('ticktock')
    print(n)
    pass


timer(5)
