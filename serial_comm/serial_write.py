import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
# ser.write(b'hello')


while True:
    ser.write(b'A')
    ser.wait(3)
    ser.write(b'S')
    False

ser.close() # Port schliessen
