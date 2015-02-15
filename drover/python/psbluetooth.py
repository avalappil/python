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


typeForArduino = "";
dataForArduino = "";

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
      #time.sleep(0.5)
      #print typeForArduino
      #print dataForArduino
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
          ##### lef joy stick - camera control
          elif event.axis == 1:
            up = float("{0:.2f}".format(event.value))
            UpdateServo = 1
          elif event.axis == 0:
            rotate = float("{0:.2f}".format(event.value))
            UpdateServo = 1

          if UpdateServo:
            if (up > threshold):
              print "up: "
              print up
            elif (up < -threshold):
              print "down: "
              print up
            elif (rotate > threshold):
              print "left: "
              print rotate
            elif (rotate < -threshold):
              print "right: "
              print rotate



          # Check if we need to update what the motors are doing
          if UpdateMotors:
            if (forward > threshold):
              print "reverse: "
              print forward
              typeForArduino = "f"
              dataForArduino = str(forward)
              drive("f",str(forward))
            elif (forward < -threshold):
              print "forward: "
              print  forward
              typeForArduino = "f"
              dataForArduino = str(forward)
              drive("f",str(forward))
            elif (turn > threshold):
              print "right: "
              print turn
              typeForArduino = "t"
              dataForArduino = str(turn)
              drive("t",str(turn))
            elif (turn < -threshold):
              print "left: "
              print turn
              typeForArduino = "t"
              dataForArduino = str(turn)
              drive("t",str(turn))
            #else:
              #typeForArduino = "t"
              #dataForArduino = "0"

except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
