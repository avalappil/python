#!/usr/bin/env python

import pygame
import time
import os
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# cam position
tilt = 1500
pan = 1500
# Set which GPIO pins the drive outputs are connected
PWMA = 17
AIN1 = 27
AIN2 = 4
PWMB = 23
BIN1 = 24
BIN2 = 25
STBY = 22
##
### Set all the drive pins as output pins
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT) 
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

# initialize Serial driver
serialC = serial.Serial('/dev/ttyAMA0', 9600)

# Initialise the pygame library
pygame.init()
# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()

threshold = 0.30

print 'Initialized Joystick : %s' % j.get_name()


typeForArduino = ""
dataForArduino = ""

typeForServo = ""
dataForServo = ""

# Configure the motors to match the current settings.
def drive(typ, data):
  print data
  serialC.write(typ)
  serialC.write(data)
  serialC.write("#")
  serialC.flush()

def forward():
  (GPIO.output(AIN1, GPIO.HIGH))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.HIGH))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def reverse():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.HIGH))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.HIGH))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def left():
  (GPIO.output(AIN1, GPIO.HIGH))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.HIGH))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def right():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.HIGH))
  (GPIO.output(BIN1, GPIO.HIGH))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.HIGH))

def leftonly():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.HIGH))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.LOW))
  (GPIO.output(PWMB, GPIO.HIGH))

def rightonly():
  (GPIO.output(AIN1, GPIO.HIGH))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.HIGH))
  (GPIO.output(PWMA, GPIO.HIGH))
  (GPIO.output(PWMB, GPIO.LOW))

def off():
  (GPIO.output(AIN1, GPIO.LOW))
  (GPIO.output(AIN2, GPIO.LOW))
  (GPIO.output(BIN1, GPIO.LOW))
  (GPIO.output(BIN2, GPIO.LOW))
  (GPIO.output(STBY, GPIO.LOW))
  (GPIO.output(PWMA, GPIO.LOW))
  (GPIO.output(PWMB, GPIO.LOW))


# Try and run the main code, and in case of failure we can stop the motors
try:
    #reset servo
    serialC.write("#23P1500T1000\r\n")
    serialC.flush()
    serialC.write("#24P1500T1000\r\n")
    serialC.flush()
    # This is the main loop
    while True:
      events = pygame.event.get()
      for event in events:
        UpdateMotors = 1
        straight = 0
        turn = 0
        L2 = 0
        R2 = 0
        # Check if one of the joysticks has moved
        if event.type == pygame.JOYAXISMOTION:
          ##### right joy stick - robot control
          straight = j.get_axis(3)
          turn = j.get_axis(2) 
          straight = float("{0:.2f}".format(straight))
          turn = float("{0:.2f}".format(turn))
          print straight
          print turn 

          ##### left joy stick - cam control
          rotate = j.get_axis(0)
          up = j.get_axis(1) 
          rotate = float("{0:.2f}".format(rotate))
          up = float("{0:.2f}".format(up))
          print rotate
          print up

          if (up > threshold):
            print "up: "
            print up
            tilt = tilt - 10
            print tilt
            if (tilt >= 1240):
              data = "#24P" + str(tilt) + "T100"
              serialC.write(data)
              serialC.write("\r\n")
              serialC.flush()
              time.sleep(0.1)
            else:
              tilt = 1240
          elif (up < -threshold):
            print "down: "
            print  up
            tilt = tilt + 10
            print tilt
            if (tilt < 2240):
              data = "#24P" + str(tilt) + "T100"
              serialC.write(data)
              serialC.write("\r\n")
              serialC.flush()
              time.sleep(0.1)
            else:
              tilt = 2240;
          elif (rotate > threshold):
            print "pan right: "
            print rotate
            drive("b",str(rotate))
          elif (rotate < -threshold):
            print "pan left: "
            print rotate
            drive("b",str(rotate))

          L2 = j.get_button(8)
          R2 = j.get_button(9)

          print L2
          print R2 

          if (L2 == 1):
            leftonly()
          elif (R2 == 1):
            rightonly()
          elif (straight > threshold):
            print "reverse: "
            reverse()
          elif (straight < -threshold):
            print "straight: "
            forward()
          elif (turn > threshold):
            print "right: "
            left()
          elif (turn < -threshold):
            print "left: "
            right()
          else:
            off()

except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
    GPIO.cleanup()
