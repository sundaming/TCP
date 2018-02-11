
from greenlet import greenlet
from time import sleep
def testA():
    while True:
        print('---------------a1')
        g2.switch()
        print('----------------a2')
        sleep(0.5)
def testB():
    while True:
        print('-----------b1')
        g1.switch()
        print('------------b2')
        sleep(0.5)
g1 = greenlet(testA)
g2 = greenlet(testB)
g2.switch()