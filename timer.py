import threading
from datetime import datetime
import random


def timer_A_pause():
    timer1.cancel()


def fun_timer_A():
    temp = random.random()
    ticktock(temp)
    global timer1
    timer1 = threading.Timer(5, fun_timer_A)
    timer1.start()


def ticktock(n):
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    print('ticktock')
    print(n)


def fun_timer_B():
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    print("123")
    fun_timer_A()


class MXZTimer():
    def __init__(self):
        pass

    def start(self, p_delay=int):
        if p_delay == 0:
            fun_timer_A()
        else:
            timer1 = threading.Timer(p_delay, fun_timer_A)
            timer1.start()

    def stop(self, p_stop_time=int):
        timer2 = threading.Timer(p_stop_time, timer_A_pause)
        timer2.start()

    def resume(self, p_pausr_time:int, p_resume_time:int):
        timer2 = threading.Timer(p_pausr_time, timer_A_pause)
        timer3 = threading.Timer(p_resume_time, fun_timer_B)
        timer2.start()
        timer3.start()

# timer1 = threading.Timer(1, fun_timer_A)
# timer2 = threading.Timer(30, timer_A_pause)
# timer3 = threading.Timer(60, fun_timer_B)
# timer1.start()
# timer2.start()
# timer3.start()

