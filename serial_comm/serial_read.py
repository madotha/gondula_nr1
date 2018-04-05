import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)

while True:
    x = ser.readline()
    print(x)
