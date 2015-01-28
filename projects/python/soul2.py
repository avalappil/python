import webiopi
import os,time
import subprocess

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyAMA0", 9600)

def setup():
    os.system ("espeak 'Started'")
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readString()

@webiopi.macro
def loadData(str):
    print (str)
    if (str == "a"):
    	serial.write(bytes("PL 1 SQ 14 ONCE\r", 'UTF-8'))
    elif (str == "b"):
    	serial.write(bytes("PL 1 SQ 23 ONCE\r", 'UTF-8'))
    elif (str == "c"):
    	serial.write(bytes("PL 1 SQ 15 ONCE\r", 'UTF-8'))
    elif (str == "d"):
    	serial.write(bytes("PL 1 SQ 4 ONCE\r", 'UTF-8'))
    elif (str == "e"):
    	serial.write(bytes("PL 1 SQ 5 ONCE\r", 'UTF-8'))
    elif (str == "f"):
    	serial.write(bytes("PL 1 SQ 12 ONCE\r", 'UTF-8'))
    elif (str == "g"):
    	serial.write(bytes("PL 1 SQ 0 ONCE\r", 'UTF-8'))
    elif (str == "h"):
    	serial.write(bytes("PL 1 SQ 13 ONCE\r", 'UTF-8'))
    elif (str == "i"):
    	serial.write(bytes("PL 1 SQ 9 ONCE\r", 'UTF-8'))
    elif (str == "j"):
    	serial.write(bytes("PL 1 SQ 8 ONCE\r", 'UTF-8'))
    elif (str == "k"):
    	serial.write(bytes("PL 1 SQ 1 ONCE\r", 'UTF-8'))
    elif (str == "l"):
    	serial.write(bytes("PL 1 SQ 2 ONCE\r", 'UTF-8'))
    elif (str == "m"):
    	serial.write(bytes("PL 1 SQ 3 ONCE\r", 'UTF-8'))
    elif (str == "n"):
    	serial.write(bytes("PL 1 SQ 16 ONCE\r", 'UTF-8'))
    elif (str == "o"):
    	serial.write(bytes("PL 1 SQ 17 ONCE\r", 'UTF-8'))
    elif (str == "p"):
    	serial.write(bytes("PL 1 SQ 19 ONCE\r", 'UTF-8'))
    elif (str == "q"):
    	serial.write(bytes("PL 1 SQ 21 ONCE\r", 'UTF-8'))
    elif (str == "r"):
    	serial.write(bytes("PL 1 SQ 1 ONCE\r", 'UTF-8'))
    elif (str == "s"):
    	serial.write(bytes("PL 1 SQ 10 ONCE\r", 'UTF-8'))
    elif (str == "t"):
    	serial.write(bytes("PL 1 SQ 20 ONCE\r", 'UTF-8'))
    elif (str == "u"):
    	serial.write(bytes("PL 1 SQ 6 ONCE\r", 'UTF-8'))
    elif (str == "v"):
    	serial.write(bytes("PL 1 SQ 7 ONCE\r", 'UTF-8'))
    #elif (str == "w"):
    	#serial.write(bytes("PL 1 SQ 1 ONCE\r", 'UTF-8'))
    #elif (str == "x"):
    #elif (str == "y"):
