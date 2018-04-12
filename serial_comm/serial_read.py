import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)

def readLine(self):
    while True:
        x = ser.readline()
        print(x)