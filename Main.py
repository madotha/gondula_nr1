import threading
from FreedomCommunication import FreedomCommunications
import cap
import time

x = 45
y = 0


def Main():
    global fc
    fc = FreedomCommunications()


def readCords():
    while True:
        fc = FreedomCommunications()
        global x
        x = fc.getXCords()
        time.sleep(1)


if __name__ == "__main__":
    Main()
