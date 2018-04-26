import serial
import time

class FreedomCommunications:

    def __init__(self):
        print("Öffne Kommunikation zu Freedom Board")
        conn = serial.Serial('/dev/ttyACM0') # Port aktualisieren
        print("Verbindung zu " + conn.name + " erfolgreich.")

    def start(self):
        print("Starte Gondula #1...")
        self.conn.write(b's')

    def stop(self):
        print("Stoppe Gondula #1...")
        self.conn.write(b'h')

    def object_detected(self):
        print("Zielobjekt wurde erkannt...")
        self.conn.write(b'd')

    def device_slower(self):
        print("Fahrzeug wird langsamer...")
        self.conn.write(b'-')

    def device_faster(self):
        print("Fahrzeug wird schneller...")
        self.conn.write(b'+')

    def getCords(self):
        self.conn.write(b'x')
        line = self.conn.readline().decode()
        print(int(line))
        time.sleep(0.1)
        self.conn.write(b'z')
        line = self.conn.readline().decode()
        z = int(line)
        print(z)

    def close_port(self):
        self.conn.close()

if __name__ == '__main__':
    FreedomCommunications.__init__(FreedomCommunications)
