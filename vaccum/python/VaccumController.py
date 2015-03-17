import webiopi
import os,time

nfaces = "0"

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyS0", 9600)
def setup():
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readstrDataing()

@webiopi.macro
def loadData(strData):
    print (strData)
    if (strData == "1"):
      serial.write(bytes("1\r\n", 'UTF-8'))
    elif (strData == "2"):
      serial.write(bytes("2\r\n", 'UTF-8'))
    elif (strData == "3"):
      serial.write(bytes("3\r\n", 'UTF-8'))
    elif (strData == "4"):
      serial.write(bytes("4\r\n", 'UTF-8'))
    elif (strData == "5"):
      serial.write(bytes("5\r\n", 'UTF-8'))
    elif (strData == "6"):
      serial.write(bytes("6\r\n", 'UTF-8'))
    elif (strData == "7"):
      serial.write(bytes("7\r\n", 'UTF-8'))
    elif (strData == "8"):
      serial.write(bytes("8\r\n", 'UTF-8'))
    elif (strData == "9"):
      serial.write(bytes("9\r\n", 'UTF-8'))