from greenlet import greenlet
import time

def test1():
    while True:
        print("--A--")
        gr1.switch()
        time.sleep(0.5)

def test2():
    while True:
        print("---B----")
        gr2.switch()
        time.sleep(0.5)
gr1=greenlet(test2)
gr2=greenlet(test1)

gr2.switch()#切换到gr1中运行