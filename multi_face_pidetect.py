import cv2
import sys
import picamera
from SimpleCV import *
import time
# Get user supplied values
imagePath = 'foto.jpg'
cascPath = 'haarcascade_frontalface_default.xml'
cascPath = LAUNCH_PATH + "/" + "Features/HaarCascades/face.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

keeprunning = 0
with picamera.PiCamera() as camera:
	camera.resolution = (320, 240)
	camera.start_preview()
	while keeprunning==0:
		time.sleep(1)
		camera.capture('foto.jpg')
		foto=Image("foto.jpg")		
		foto.save('foto.jpg') 
		#foto.show()
		# Read the image
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(30, 30),
		    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)

		print "Found {0} faces!".format(len(faces))
	camera.stop_preview()