import time
import SimpleCV
from SimpleCV import *
display = SimpleCV.Display()
cam = SimpleCV.Camera()

cascade = LAUNCH_PATH + "/" + "Features/HaarCascades/face.xml"
haarcascade = SimpleCV.HaarCascade(cascade) 

while display.isNotDone():
	time.sleep(1)
	image = cam.getImage().flipHorizontal().scale(0.5)
	faces = image.findHaarFeatures(haarcascade)
	if faces:
		face = faces.sortArea()
		face.draw(SimpleCV.Color.RED, 1)
	
	image.show()