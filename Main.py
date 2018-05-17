# import threading
# import FreedomCommunication as fc
# import cap
# import time
import GUI

X_START = 45
Z_START = 0


def Main():

    # fc.init()
    # cap.start()
    GUI.start(readCords)




test = 0
def readCords():
    # x = fc.getXCords()
    # if x > X_START:
    #     return x
    # return X_START
    global test
    test += 5
    print(test)
    return test


if __name__ == "__main__":
    Main()
