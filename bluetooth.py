import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
while True :
    try:
        state=ser.read()
        print(state)
    except:
        pass