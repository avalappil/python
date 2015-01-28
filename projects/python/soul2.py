import webiopi
import os,time
import subprocess

# import Serial driver
from webiopi.devices.serial import Serial

headPos = 1500
minPos = 550
maxPos = 2400
# initialize Serial driver
serial = Serial("ttyAMA0", 9600)
def setup():
    headPos = 1500
    minPos = 550
    maxPos = 2400
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readString()

@webiopi.macro
def loadData(str):
    print (str)
    if (str == "0"):
    	serial.write(bytes("PL 1 SQ 0 ONCE\r", 'UTF-8'))
    elif (str == "1"):
    	serial.write(bytes("PL 1 SQ 1 ONCE\r", 'UTF-8'))
    elif (str == "2"):
    	serial.write(bytes("PL 1 SQ 2 ONCE\r", 'UTF-8'))
    elif (str == "3"):
    	serial.write(bytes("PL 1 SQ 3 ONCE\r", 'UTF-8'))
    elif (str == "4"):
    	serial.write(bytes("PL 1 SQ 4 ONCE\r", 'UTF-8'))
    elif (str == "5"):
    	serial.write(bytes("PL 1 SQ 5 ONCE\r", 'UTF-8'))
    elif (str == "6"):
    	serial.write(bytes("PL 1 SQ 6 ONCE\r", 'UTF-8'))
    elif (str == "7"):
    	serial.write(bytes("PL 1 SQ 7 ONCE\r", 'UTF-8'))
    elif (str == "8"):
    	serial.write(bytes("PL 1 SQ 8 ONCE\r", 'UTF-8'))
    elif (str == "9"):
    	serial.write(bytes("PL 1 SQ 9 ONCE\r", 'UTF-8'))
    elif (str == "10"):
    	serial.write(bytes("PL 1 SQ 10 ONCE\r", 'UTF-8'))
    elif (str == "11"):
    	serial.write(bytes("PL 1 SQ 11 ONCE\r", 'UTF-8'))
    elif (str == "12"):
    	serial.write(bytes("PL 1 SQ 12 ONCE\r", 'UTF-8'))
    elif (str == "13"):
    	serial.write(bytes("PL 1 SQ 13 ONCE\r", 'UTF-8'))
    elif (str == "14"):
    	serial.write(bytes("PL 1 SQ 14 ONCE\r", 'UTF-8'))
    elif (str == "15"):
    	serial.write(bytes("PL 1 SQ 15 ONCE\r", 'UTF-8'))
    elif (str == "16"):
    	serial.write(bytes("PL 1 SQ 16 ONCE\r", 'UTF-8'))
    elif (str == "17"):
    	serial.write(bytes("PL 1 SQ 17 ONCE\r", 'UTF-8'))
    elif (str == "18"):
    	serial.write(bytes("PL 1 SQ 18 ONCE\r", 'UTF-8'))
    elif (str == "19"):
    	serial.write(bytes("PL 1 SQ 19 ONCE\r", 'UTF-8'))
    elif (str == "20"):
    	serial.write(bytes("PL 1 SQ 20 ONCE\r", 'UTF-8'))
    elif (str == "l"):
        headPos = headPos - 1
        if (headPos < minPos):
            headPos = minPos
        serial.write(bytes("P#15 P" + str(headPos) +" T1000\r", 'UTF-8'))
    elif (str == "r"):
        headPos = headPos + 1
        if (headPos > maxPos):
            headPos = maxPos
        serial.write(bytes("P#15 P" + str(headPos) +" T1000\r", 'UTF-8'))
    #elif (str == "x"):
    #elif (str == "y"):
