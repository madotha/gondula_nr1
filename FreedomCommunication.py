import serial
import time


def init():
    print("Öffne Kommunikation zu Freedom Board")
    global conn
    conn = serial.Serial('/dev/ttyACM0')  # Port aktualisieren
    print("Verbindung zu " + conn.name + " erfolgreich.")


def start():
    print("Starte Gondula #1...")
    conn.write(b's')


def stop():
    print("Stoppe Gondula #1...")
    conn.write(b'h')


def object_detected():
    print("Zielobjekt wurde erkannt...")
    conn.write(b'd')


def device_slower():
    print("Fahrzeug wird langsamer...")
    conn.write(b'-')


def device_faster():
    print("Fahrzeug wird schneller...")
    conn.write(b'+')


def getXCords():
    conn.write(b'x')
    lineX = conn.readline().decode()
    return (int(lineX))


def getZCords():
    conn.write(b'z')
    lineZ = conn.readline().decode()
    return (int(lineZ))


def getCords():
    x = getXCords()
    time.sleep(0.1)
    z = getZCords()
    return x, z


def close_port():
    conn.close()

# if __name__ == "__main__":
#     main()
