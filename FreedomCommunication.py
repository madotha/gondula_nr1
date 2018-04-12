import serial
import time

def __init__(self):
    print("Öffne Kommunikation zu Freedom Board")
    conn = serial.Serial('/dev/ttyACM0') # Port aktualisieren
    print("Verbindung zu " + conn.name + " erfolgreich.")

def start(self):
    print("Starte Gondula #1...")
    self.conn.write(b'S')

def stop(self):
    print("Stoppe Gondula #1...")
    self.conn.write(b'H')

def object_detected(self):
    print("Zielobjekt wurde erkannt...")
    self.conn.write(b'D')

def device_slower(self):
    print("Fahrzeug wird langsamer...")
    self.conn.write(b'-')

def device_faster(self):
    print("Fahrzeug wird schneller...")
    self.conn.write(b'+')


