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

threshold = 0.60

print 'Initialized Joystick : %s' % j.get_name()

# Setup the various GPIO values, using the BCM numbers for now
left = 16
MotorA1 = 18
MotorAE = 22

MotorB0 = 23
MotorB1 = 21
MotorBE = 19

# Configure the motors to match the current settings.
def setmotors(data):
  print data
  serialC.write(bytes("Leftforward\r\n", 'UTF-8'))

# Try and run the main code, and in case of failure we can stop the motors
try:
    # This is the main loop
    while True:

        # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0
          RightTrack = 0
          LeftTrack = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
              LeftTrack = event.value
              UpdateMotors = 1
            elif event.axis == 3:
              RightTrack = event.value
              UpdateMotors = 1

            # Check if we need to update what the motors are doing
            if UpdateMotors:
              # Check how to configure the left motor

              # Move forwards
              if (RightTrack > threshold):
                print "Right: "
                print RightTrack
              # Move backwards
              elif (RightTrack < -threshold):
                print "Right: "
                print RightTrack
              # Stopping
              else:
                  A0 = False
                  A1 = False

              # And do the same for the right motor
              if (LeftTrack > threshold):
                print "Left: "
                print LeftTrack
              # Move backwards
              elif (LeftTrack < -threshold):
                print "Left: "
                print LeftTrack
              # Otherwise stop
              else:
                  B0 = False
                  B1 = False

              # Now we've worked out what is going on we can tell the
              # motors what they need to do
              #setmotors()


except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python
