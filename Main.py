# import threading
import FreedomCommunication as fc
import cap
# import time
import GUI

x_pos = 45
z_pos = 0


def Main():

    # fc.init()
    # cap.start()
    GUI.start(fc.start, getCords)




def readCords():
    global x_pos
    global z_pos
    first_match = False
    while True:
        x, z = fc.getCords()
        if x > x_pos:
            x_pos = x
            if first_match:
                cap.start()

        z_pos = z

def getCords():
    return x_pos, z_pos





if __name__ == "__main__":
    Main()
