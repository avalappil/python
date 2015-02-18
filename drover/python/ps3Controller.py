#!/usr/bin/env python

import pygame
import time
import os
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

servoMap = {1.00:"400",0.90:"500",0.80:"600",0.70:"700",0.60:"900",0.50:"1000",0.40:"1100",0.30:"1200",0.20:"1300",0.10:"1400",-0.10:"1600",-0.20:"1700",-0.30:"1800",-0.40:"1900",-0.50:"2000",-0.60:"2100",-0.70:"2200",-0.80:"2300",-0.90:"2400",-1.00:"2500"}

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
      #off()
      #time.sleep(1)
      events = pygame.event.get()
      for event in events:
        UpdateMotors = 1
        straight = 0
        turn = 0
        L2 = 0
        R2 = 0
        rotate = 0
        up = 0
        UpdateServo = 0
        # Check if one of the joysticks has moved
        if event.type == pygame.JOYAXISMOTION:
          ##### right joy stick - robot control
          straight = j.get_axis(3)
          turn = j.get_axis(2) 
          straight = float("{0:.2f}".format(straight))
          turn = float("{0:.2f}".format(turn))

          #if event.axis == 2:
          #  turn = float("{0:.2f}".format(event.value))
          #  UpdateMotors = 1
          #elif event.axis == 3:
          #  straight = float("{0:.2f}".format(event.value))
          #  UpdateMotors = 1

          ##### right joy stick - robot control
          if event.axis == 0:
            rotate = float("{0:.2f}".format(event.value))
            UpdateServo = 1
          elif event.axis == 1:
            up = float("{0:.2f}".format(event.value))
            UpdateServo = 1

          print straight, turn 

          #print rotate
          #print up

          L2 = j.get_button(8)
          R2 = j.get_button(9)

          #print L2
          #print R2 



          if (UpdateMotors):
            if (L2 == 1):
              leftonly()
            elif (R2 == 1):
              rightonly()            
            elif (straight > threshold):
              print "reverse: "
              reverse()
              #time.sleep(0.1)
            elif (straight < -threshold):
              print "straight: "
              forward()
              #time.sleep(0.1)
            elif (turn > threshold):
              print "right: "
              left()
              #time.sleep(0.1)
            elif (turn < -threshold):
              print "left: "
              right()
            else:
              off()
          else:
            off()

except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
    GPIO.cleanup()
