import threading
import FreedomCommunication
#import cap
import time
import GUI

x = 45
y = 0


def Main():
    global fc
    fc = FreedomCommunication
    while True:
        fc.getXCords()
        fc.getZCords()
    global gui
    gui = GUI


def readCords():
    while True:
        fc = FreedomCommunication
        global x
        x = fc.getXCords()
        time.sleep(1)


if __name__ == "__main__":
    Main()
