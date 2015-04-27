import webiopi
import os,time

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyAMA0", 9600)
def setup():
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readstrDataing()

@webiopi.macro
def positionhead(strData):
    print (strData)
    if (strData != "" and strData.startswith('l')):
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
