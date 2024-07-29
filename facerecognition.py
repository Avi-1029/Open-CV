import cv2
import os
import numpy as np

mainfolder = 'database'
xmlfile = "haarcascade_frontalface_default.xml"

#print(list(os.walk(mainfolder)))
id = 0
names = {}
images = []
labels = []

for root, subfolders, files in os.walk(mainfolder):
    #print(root)
    #print(subfolders)
    #print(files)

    for subfolder in subfolders:
        names[id] = subfolder
        path = os.path.join(mainfolder,subfolder)
        for file in os.listdir(path):
            image = cv2.imread(os.path.join(path,file),0)
            images.append(image)
            labels.append(id)
        id = id + 1
       
#print(names)
#print(labels)

images = np.array(images)
labels = np.array(labels)

width = 100
height = 130

model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)
xmlfile = "haarcascade_frontalface_default.xml"
facedet = cv2.CascadeClassifier(xmlfile)
video = cv2.VideoCapture(0)

while True:
    r, i = video.read()
    sadimg = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    face = facedet.detectMultiScale(sadimg, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(i, (x,y),(x+w, y+h), (255,255,255), 3)
        values = sadimg[y:y+h, x:x+w]
        newface = cv2.resize(values, (width,height))

        prediction, confidence =  model.predict(newface)
        print(prediction)

    cv2.imshow('...', i)
    key = cv2.waitKey(10)
    if key == 27:
        break
 

  