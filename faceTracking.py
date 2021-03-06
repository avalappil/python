from SimpleCV import *
import time
"""
This is an example of HOW-TO use FaceRecognizer to recognize gender
of the person.
"""
cascade = LAUNCH_PATH + "/" + "Features/HaarCascades/face.xml"

f = FaceRecognizer()
cam = Camera()
f.load(LAUNCH_PATH + "/" + "Features/FaceRecognizerData/GenderData.xml")
w, h = f.imageSize
draw_color = Color.YELLOW

def identifyGender():
    img = cam.getImage().flipHorizontal().scale(0.5)
    feat = img.findHaarFeatures(cascade)
    if feat:
        i = 0
        for trovato in feat:
            i = i + 1
        crop_image = feat.sortArea()[-1].crop()
        #feat.sortArea()[-1].draw()
        crop_image = crop_image.resize(w, h)
        label, confidence = f.predict(crop_image)
        img.dl().selectFont('purisa')
        if label == 0:
            print "Female"
            img.drawText("Female" +  str(i) + " faces", color=draw_color,fontsize=24)
        else:
            print "Male"
            img.drawText("Male"  +  str(i) + " faces", color=draw_color,fontsize=24)
    else:
        img.drawText("No face detected", color=draw_color,fontsize=24)
    img.show()

keeprunning = 0
while keeprunning==0:
    identifyGender()