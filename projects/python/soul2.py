import webiopi
import os,time

nfaces = "0"

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyAMA0", 9600)
def setup():
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readstrDataing()

@webiopi.macro
def setfaces(aData):
    global nfaces
    nfaces = aData

@webiopi.macro
def numoffaces(aData):
    global nfaces
    return nfaces

@webiopi.macro
def loadData(strData):
    print (strData)
    if (strData == "0"):
    	serial.write(bytes("PL 1 SQ 0 ONCE\r", 'UTF-8'))
    elif (strData == "1"):
    	serial.write(bytes("PL 1 SQ 1 ONCE\r", 'UTF-8'))
    elif (strData == "2"):
    	serial.write(bytes("PL 1 SQ 2 ONCE\r", 'UTF-8'))
    elif (strData == "3"):
    	serial.write(bytes("PL 1 SQ 3 ONCE\r", 'UTF-8'))
    elif (strData == "4"):
    	serial.write(bytes("PL 1 SQ 4 ONCE\r", 'UTF-8'))
    elif (strData == "5"):
    	serial.write(bytes("PL 1 SQ 5 ONCE\r", 'UTF-8'))
    elif (strData == "6"):
    	serial.write(bytes("PL 1 SQ 6 ONCE\r", 'UTF-8'))
    elif (strData == "7"):
    	serial.write(bytes("PL 1 SQ 7 ONCE\r", 'UTF-8'))
    elif (strData == "8"):
    	serial.write(bytes("PL 1 SQ 8 ONCE\r", 'UTF-8'))
    elif (strData == "9"):
    	serial.write(bytes("PL 1 SQ 9 ONCE\r", 'UTF-8'))
    elif (strData == "10"):
    	serial.write(bytes("PL 1 SQ 10 ONCE\r", 'UTF-8'))
    elif (strData == "11"):
    	serial.write(bytes("PL 1 SQ 11 \r", 'UTF-8'))
    elif (strData == "12"):
    	serial.write(bytes("PL 1 SQ 12 ONCE\r", 'UTF-8'))
    elif (strData == "13"):
    	serial.write(bytes("PL 1 SQ 13 ONCE\r", 'UTF-8'))
    elif (strData == "14"):
    	serial.write(bytes("PL 1 SQ 14 ONCE\r", 'UTF-8'))
    elif (strData == "15"):
    	serial.write(bytes("PL 1 SQ 15 ONCE\r", 'UTF-8'))
    elif (strData == "16"):
    	serial.write(bytes("PL 1 SQ 16 ONCE\r", 'UTF-8'))
    elif (strData == "17"):
    	serial.write(bytes("PL 1 SQ 17 ONCE\r", 'UTF-8'))
    elif (strData == "18"):
    	serial.write(bytes("PL 1 SQ 18 ONCE\r", 'UTF-8'))
    elif (strData == "19"):
    	serial.write(bytes("PL 1 SQ 19 ONCE\r", 'UTF-8'))
    elif (strData == "20"):
    	serial.write(bytes("PL 1 SQ 20 \r", 'UTF-8'))
    elif (strData == "21"):
        serial.write(bytes("PL 1 SQ 21 ONCE\r", 'UTF-8'))
    elif (strData == "22"):
        serial.write(bytes("PL 1 SQ 22 ONCE\r", 'UTF-8'))
    elif (strData == "23"):
        serial.write(bytes("PL 1\r", 'UTF-8')) #stop the player
    elif (strData != "" and strData.startswith('l')):        
        headPos = strData.split('@')
        data = "#15 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    elif (strData != "" and strData.startswith('r')):
        headPos = strData.split('@')
        data = "#15 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    elif (strData != "" and strData.startswith('t')):
        headPos = strData.split('@')
        data = "#31 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    elif (strData != "" and strData.startswith('b')):
        headPos = strData.split('@')
        data = "#31 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8')) 
    elif (strData != "" and strData.startswith('d')):
        headPos = strData.split('@')
        data = "#24 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))     
    elif (strData != "" and strData.startswith('e')):
        headPos = strData.split('@')
        data = "#8 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))     
    elif (strData != "" and strData.startswith('f')):
        headPos = strData.split('@')
        data = "#9 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))     
    elif (strData != "" and strData.startswith('g')):
        headPos = strData.split('@')
        data = "#25 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))     
    elif (strData != "" and strData.startswith('h')):
        headPos = strData.split('@')
        data = "#10 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))     
    elif (strData != "" and strData.startswith('i')):
        headPos = strData.split('@')
        data = "#26 P" + headPos[1] + " T1000"
        webiopi.debug(data)
        serial.write(bytes(data + "\r", 'UTF-8'))
    #elif (strData == "x"):
    #elif (strData == "y"):