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

# Try and run the main code, and in case of failure we can stop the motors
try:
    # This is the main loop
    while True:

      events = pygame.event.get()
      for event in events:
        UpdateMotors = 0
        forward = 0
        turn = 0
        UpdateServo = 0
        up = 0
        rotate = 0
        # Check if one of the joysticks has moved
        if event.type == pygame.JOYAXISMOTION:
          ##### right joy stick - robot control
          if event.axis == 2:
            turn = float("{0:.2f}".format(event.value))
            UpdateMotors = 1
          elif event.axis == 3:
            forward = float("{0:.2f}".format(event.value))
            UpdateMotors = 1

          # Check if we need to update what the motors are doing
          if UpdateMotors:
            if (forward > threshold):
              print "reverse: "
              print forward
              drive("f",str(forward))
            elif (forward < -threshold):
              print "forward: "
              print  forward
              drive("f",str(forward))
            elif (turn > threshold):
              print "right: "
              print turn
              drive("t",str(turn))
            elif (turn < -threshold):
              print "left: "
              print turn
              drive("t",str(turn))

except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
