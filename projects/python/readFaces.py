import time
import cv2
import sys
import SimpleCV
from SimpleCV import *
import urllib

cascade = "/home/pi/Code/SimpleCV/SimpleCV/Features/HaarCascades/face.xml"
URL = "http://10.0.1.17:8421/?action=snapshot"
imgName = "snapShotImg.jpg"
faceCascade = cv2.CascadeClassifier(cascade)
username = 'webiopi'
password = 'raspberry'

url = "http://10.0.1.17:8000/macros/setfaces/"

while True:	
	try:
		urllib.urlretrieve(URL, imgName)
		time.sleep(2)
		print ("Image Saved")
		image = cv2.imread(imgName)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
	    	gray,
	    	scaleFactor=1.1,
	    	minNeighbors=5,
	    	minSize=(30, 30),
	    	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		#print (len(faces))
		str = url + str(len(faces))
		print (str)
		#r = requests.post(str, auth=(username, password))
	except:
		pass