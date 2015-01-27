import webiopi
import os,time

# import Serial driver
from webiopi.devices.serial import Serial

# initialize Serial driver
serial = Serial("ttyAMA0", 9600)

def setup():
    os.system ("espeak 'Started'")
    # empty input buffer before starting processing
    while (serial.available() > 0):
        serial.readString()
#    webiopi.sleep(1)

@webiopi.macro
def loadData(str):
    print (str)
    if (str == "a"):
    	serial.write("PL 1 SQ 14 ONCE<CR>")
    elif (str == "b"):
    	serial.write("PL 1 SQ 23 ONCE<CR>")
    elif (str == "c"):
    	serial.write("PL 1 SQ 15 ONCE<CR>")
    elif (str == "d"):
    	serial.write("PL 1 SQ 4 ONCE<CR>")
    elif (str == "e"):
    	serial.write("PL 1 SQ 5 ONCE<CR>")
    elif (str == "f"):
    	serial.write("PL 1 SQ 12 ONCE<CR>")
    elif (str == "g"):
    	serial.write("PL 1 SQ 0 ONCE<CR>")
    elif (str == "h"):
    	serial.write("PL 1 SQ 13 ONCE<CR>")
    elif (str == "i"):
    	serial.write("PL 1 SQ 9 ONCE<CR>")
    elif (str == "j"):
    	serial.write("PL 1 SQ 8 ONCE<CR>")
    elif (str == "k"):
    	serial.write("PL 1 SQ 1 ONCE<CR>")
    elif (str == "l"):
    	serial.write("PL 1 SQ 2 ONCE<CR>")
    elif (str == "m"):
    	serial.write("PL 1 SQ 3 ONCE<CR>")
    elif (str == "n"):
    	serial.write("PL 1 SQ 16 ONCE<CR>")
    elif (str == "o"):
    	serial.write("PL 1 SQ 17 ONCE<CR>")
    elif (str == "p"):
    	serial.write("PL 1 SQ 19 ONCE<CR>")
    elif (str == "q"):
    	serial.write("PL 1 SQ 21 ONCE<CR>")
    elif (str == "r"):
    	serial.write("PL 1 SQ 1 ONCE<CR>")
    elif (str == "s"):
    	serial.write("PL 1 SQ 10 ONCE<CR>")
    elif (str == "t"):
    	serial.write("PL 1 SQ 20 ONCE<CR>")
    elif (str == "u"):
    	serial.write("PL 1 SQ 6 ONCE<CR>")
    elif (str == "v"):
    	serial.write("PL 1 SQ 7 ONCE<CR>")
    #elif (str == "w"):
    	#serial.write("PL 1 SQ 1 ONCE<CR>")
    #elif (str == "x"):
    	#serial.write("PL 1 SQ 1 ONCE<CR>")
    #elif (str == "y"):
    	#serial.write("PL 1 SQ 1 ONCE<CR>")
    #elif (str == "z"):
    	#serial.write("PL 1 SQ 1 ONCE<CR>")