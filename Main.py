import threading
import _thread
import FreedomCommunication as fc
import cap
import time
import GUI

BLOCK_STARTPOS = 45
x_pos = BLOCK_STARTPOS
z_pos = 0
targetnotfound = True


def Main():
    # Open Serialinterface
    time.sleep(1)
    fc.open()
    GUI.start(startGondula, getCords)


def startGondula():
    fc.start()
    print("Start blabla")
    readCordsFromSerial()




def readCordsFromSerial():
    print("read start")
    global x_pos
    global z_pos
    first_run = True
    x_compare = 0
    while targetnotfound:
        # X Values are only send from the Controller, after it pick up the Block. Until this, he sends 0
        # So the first Value after 0 gets read and safe to compare the progress, after this position.
        x, z = fc.getCords()
        if x > 0:
            # Start PictureDetection by first
            if first_run:
                x_compare, _ = x
                _thread.start_new_thread(cap.start(targetreached))
                first_run = False
            else:
                x_pos = x_compare - x + BLOCK_STARTPOS
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
