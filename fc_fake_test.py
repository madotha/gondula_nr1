import serial
import time

xfake = 100
zfake = 100
counter = 0

def open():
    print("Öffne Kommunikation zu Freedom Board")
    print("FAKE Verbindung")


def start():
    print("Starte Gondula #1...")


def stop():
    print("Stoppe Gondula #1...")


def object_detected():
    print("Zielobjekt wurde erkannt...")


def device_slower():
    print("Fahrzeug wird langsamer...")


def device_faster():
    print("Fahrzeug wird schneller...")


def getXCords():
    global counter
    if counter < 3:
        counter+=1
        return 0
    global xfake
    xfake-=1
    print(xfake)
    return xfake


def getZCords():
    global zfake
    zfake -=1
    return zfake


def getCords():
    x = getXCords()
    time.sleep(0.1)
    z = getZCords()
    return x, z


def close_port():
    print("Port geschlossen")

# if __name__ == "__main__":
#     main()
