import threading
import _thread
import FreedomCommunication as fc
import cap
import time
import GUI

x_pos = 45
z_pos = 0
targetnotfound = False

def Main():
    # Open Serialinterface
    fc.open()
    GUI.start(startGondula, getCords)


def startGondula():
    fc.start()
    readCordsFromSerial()



def readCordsFromSerial():
    global x_pos
    global z_pos
    first_run = True
    while targetnotfound:
        x, z = fc.getCords()
        if x > x_pos:
            x_pos = x
            if first_run:
                _thread.start_new_thread(cap.start(targetreached))
                first_run = False
            z_pos = z
        time.sleep(1)

def targetreached():
    fc.object_detected()
    global targetnotfound
    targetnotfound = False


def getCords():
    return x_pos, z_pos


if __name__ == "__main__":
    Main()
