from SimpleCV import *
import time
import os, sys

# This file shows you how to train Fisher Face Recognition
# Enter the names of the faces and the output file.
cascade = "/home/bananapi/Code/SimpleCV/SimpleCV/Features/HaarCascades/face.xml"
draw_color = Color.YELLOW
cam = Camera(0) # camera
#names = ['Ajith.jpg','Geetha.jpg'] # names of people to recognize
outfile = "test.csv" #output file 
waitTime = 10 # how long to wait between each training session

suffix = ".jpg"
path = "authentication"
names = []
paths = []

time.sleep(5)
labels = []
imgs = []


def getFaceRead(imgList, myStr):
    # Grab a series of faces and return them.
    # quit when we press escape. 
    iset = ImageSet()
    count = 0
    disp = Display((640,480))
    show = 1;
    for i in range(len(imgList)):
        time.sleep(2)
        img = Image(imgList[i])
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

#Read images from files
for root, directories, files in os.walk(path):
    for filename in directories:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        names.append(filename)
        paths.append(filepath)

for d in range(len(names)):
    print names[d]
    imagePaths=[]
    for rt, drts, fls  in os.walk(paths[d]):
        for flname in fls:
            flpath = os.path.join(rt, flname)
            if flpath.endswith(suffix):
                imagePaths.append(flpath)
                #print flpath
    iset = getFaceRead(imagePaths, names[d])
    imgs += iset
    labels += [names[d] for i in range(0,len(iset))]
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
