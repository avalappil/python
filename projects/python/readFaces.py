import time
import cv2
import sys
import webcolors
import SimpleCV
from SimpleCV import *
import urllib

cascade = "/home/pi/Code/SimpleCV/SimpleCV/Features/HaarCascades/face.xml"
URL = "http://raspberrypi:8421/?action=snapshot"
imgName = "snapShotImg.jpg"
faceCascade = cv2.CascadeClassifier(cascade)
username = 'webiopi'
password = 'raspberry'
print ("Starting...")

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


while True:	
	#try:
	urllib.urlretrieve(URL, imgName)
	time.sleep(2)
	print ("Image Saved")
	img = Image(imgName)
	(r, g, b) = img.getPixel(160, 120)
	requested_colour = (r, g, b)
	print(r, g, b)
	actual_name, closest_name = get_colour_name(requested_colour)
	print "Actual colour name:", actual_name, ", closest colour name:", closest_name

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
	print (len(faces))
	#except:
	#	pass