#!/usr/bin/env python

import pygame
import time
import serial

# initialize Serial driver
serialC = serial.Serial('/dev/ttyAMA0', 9600)

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()

threshold = 0.30

print 'Initialized Joystick : %s' % j.get_name()


leftMotor = 0
rightMotor = 0

typeForServo = ""
dataForServo = ""

# Configure the motors to match the current settings.
def drive(typ,leftMotor,rightMotor):
  serialC.write(typ)
  serialC.write(leftMotor)
  serialC.write("o")
  serialC.write(rightMotor)
  serialC.write("#")
  serialC.flush()


# Try and run the main code, and in case of failure we can stop the motors
try:
    # This is the main loop
    while True:
      
      events = pygame.event.get()
      for event in events:
        direction = 0 #0 go front, else go back
        turn = 0
        UpdateServo = 0
        up = 0
        rotate = 0
        # Check if one of the joysticks has moved
        if event.type == pygame.JOYAXISMOTION:
          ##### right joy stick - robot control
          forward = j.get_axis(3)
          turn = j.get_axis(2)
          forward = float("{0:.2f}".format(forward))
          turn = float("{0:.2f}".format(turn))
          forward = forward * 100
          turn = turn * 100
          forward = int(round(float(forward)))
          turn = int(round(float(turn)))

          if (forward < -threshold and turn < threshold and turn > -threshold):
            #go straight
            direction = 0
            leftMotor = (255 * (forward * -1))/100
            rightMotor = leftMotor
          elif (forward < -threshold and turn > threshold):
            #go slight right
            direction = 0
            leftMotor = (255 * (forward * -1))/100
            rightMotor = (255 * turn)/100
          elif (forward < -threshold and turn < -threshold):
            #go slight left
            direction = 0
            rightMotor = (255 * (forward * -1))/100
            leftMotor = (255 * (turn * -1))/100
          elif (forward > threshold and turn < threshold and turn > -threshold):
            #go straight
            direction = 1
            leftMotor = (255 * forward)/100
            rightMotor = leftMotor
          elif (forward > threshold and turn > threshold):
            #go slight right
            direction = 1
            leftMotor = (255 * forward)/100
            rightMotor = (255 * turn)/100
          elif (forward > threshold and turn < -threshold):
            #go slight left
            direction = 1
            rightMotor = (255 * forward)/100
            leftMotor = (255 * (turn * -1))/100
          elif (turn < -threshold and forward < threshold and forward > -threshold):
            #go slight left
            direction = 0
            leftMotor = 0
            rightMotor = (255 * (turn * -1))/100 
          elif (turn > threshold and forward < threshold and forward > -threshold):
            #go slight left
            direction = 0     
            rightMotor = 0
            leftMotor = (255 * turn)/100 
          else:
            direction = 0
            leftMotor = 0
            rightMotor = 0

          print leftMotor, " <<>> ", rightMotor, " <<>> ", direction

          if (direction == 0):
            drive("f", str(leftMotor), str(rightMotor))
          elif (direction == 1):
            drive("b", str(leftMotor), str(rightMotor))

except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
