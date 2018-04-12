import serial
import time

def __init__(self):
    print("Öffne Kommunikation zu Freedom Board")
    conn = serial.Serial('/dev/ttyACM0') # Port aktualisieren
    print("Verbindung zu " + conn.name + " erfolgreich.")

def start(self):
    print("Starte Gondula #1...")
    self.conn.write(b'ST')

def stop(self):
    print("Stoppe Gondula #1...")
    self.conn.write(b'SP')
