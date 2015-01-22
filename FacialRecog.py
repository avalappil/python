from SimpleCV import *
import time

# This file shows you how to train Fisher Face Recognition
# Enter the names of the faces and the output file.
cascade = LAUNCH_PATH + "/" + "Features/HaarCascades/face.xml"
draw_color = Color.YELLOW
cam = Camera(0) # camera
names = ['Ajith.jpg','Geetha.jpg'] # names of people to recognize
outfile = "test.csv" #output file 
waitTime = 10 # how long to wait between each training session

def getFaceRead(cam,myStr=""):
    # Grab a series of faces and return them.
    # quit when we press escape. 
    iset = ImageSet()
    count = 0
    disp = Display((640,480))
    show = 1;
    while count<3:
        time.sleep(1)
        img = Image(name)
        fs = img.findHaarFeatures(cascade)
        if fs:
            fs = fs.sortArea()
            face = fs[-1].crop().resize(100,100)
            fs[-1].draw()
            iset.append(face)
            count = count + 1
        img.drawText(myStr,20,20,color=Color.RED,fontsize=32)
        img.save(disp)   
    disp.quit()
    return iset    

# First make sure our camera is all set up.
#getFaceSet(cam,"Get Camera Ready! - ESC to Exit")
time.sleep(5)
labels = []
imgs = []
# for each person grab a training set of images
# and generate a list of labels.
for name in names:
    myStr = "Training for : " + name
    iset = getFaceRead(cam,name)
    imgs += iset
    labels += [name for i in range(0,len(iset))]
    time.sleep(waitTime)

# Create, train, and save the recognizer. 
f = FaceRecognizer()
print f.train(imgs, labels)
f.save(outfile)
# Now show us the results
disp = Display((640,480))
while disp.isNotDone():
    time.sleep(1)
    img = cam.getImage()
    img.dl().selectFont('purisa')
    try:
        fs = img.findHaarFeatures(cascade)
        if fs:
            fs = fs.sortArea()
            face = fs[-1].crop().resize(100,100)
            fs[-1].draw()
            name, confidence = f.predict(face)
            if confidence > 1600:            
                img.drawText(name + "#"  + str(confidence),30,30,color=draw_color,fontsize=34)
                print ("Name: " + str(name) + " confidence: " + str(confidence))
            else:
                #img.drawText("Not recoganized: " + name + "#"  + str(confidence),30,30,color=draw_color,fontsize=34)
                print ("Name Not recoganized: confidence: " + str(confidence))                   
        img.save(disp)
    except e:
        print ("There is an exception")
