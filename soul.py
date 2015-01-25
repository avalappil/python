import serial
import time

servoSerial = serial.Serial('/dev/ttyACM0', 9600)
bluetoothSerial = serial.Serial('/dev/ttyAMA0', 9600)

def walkForward():
	time.sleep(1.1)
	servoSerial.write("#1P826#2P2087#3P1500#4P1500#5P1500#8P1500#9P1500#10P1500#14P1500#23P1500#24P1500#25P1500#28P1500#29P1500#30P1500#31P1500#32P1500T1000\r\n")
	time.sleep(1.1)
	servoSerial.write("#1P1978#2P2087#3P1500#4P1500#5P1500#8P1500#9P1500#10P1500#14P1500#23P1500#24P1500#25P1500#28P1500#29P1500#30P1500#31P1500#32P1500T1000\r\n")
	time.sleep(1.1)
	servoSerial.write("#1P1978#2P1783#3P1500#4P1500#5P1500#8P1500#9P1500#10P1500#14P1500#23P1500#24P1500#25P1500#28P1500#29P1500#30P1500#31P1500#32P1500T1000\r\n")
	time.sleep(1.1)
	servoSerial.write("#1P1065#2P1196#3P1500#4P1500#5P1500#8P1500#9P1500#10P1500#14P1500#23P1500#24P1500#25P1500#28P1500#29P1500#30P1500#31P1500#32P1500T1000\r\n")
	time.sleep(1.1)

while True :
	time.sleep(1)
	try:
		state=bluetoothSerial.read()
		if (state == "a"):
			walkForward()
		print(state)
	except:
		pass