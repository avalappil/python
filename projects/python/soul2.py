import webiopi
import os,time

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyAMA0", 9600)

def setup():
    os.system ("espeak 'hi'")
    print ("Starting")
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readString()

#def loop():
#def destroy():

#    if (serial.available() > 0):
#        line = serial.readString()     # read available data
#        print (line)
#    webiopi.sleep(1)

@webiopi.macro
def loadData(str):
    print (str)
    #os.system("espeak 'got data " + str + " ' ")
# Program will clean up all GPIO settings and terminates
# End
