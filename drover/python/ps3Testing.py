#!/usr/bin/env python

import pygame
import time
import serial

# initialize Serial driver
serialC = serial.Serial('/dev/ttyAMA0', 9600)

serialC.write("#23P")
serialC.write("1000")
serialC.write("T1000")
serialC.write("\r")
serialC.flush()
time.sleep(1)    
serialC.write("#24P800T1000\r\n")
serialC.flush()
time.sleep(1)
print "done"