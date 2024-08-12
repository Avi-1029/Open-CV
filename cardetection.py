import cv2
import os
import numpy as np

mainfolder = 'cars'
xmlfile = "cars.xml"

id = 0
names = {}
images = []
labels = []

for root, subfolders, files in os.walk(mainfolder):
   
    for subfolder in subfolders:
        names[id] = subfolder
        path = os.path.join(mainfolder,subfolder)
        for file in os.listdir(path):
            image = cv2.imread(os.path.join(path,file),0)
            images.append(image)
            labels.append(id)
        id = id + 1
       
images = np.array(images)
labels = np.array(labels)

width = 100
height = 130

car_cascade = cv2.CascadeClassifier(xmlfile)
video = cv2.VideoCapture('video.avi')

while True:
    r, img = video.read()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    car = car_cascade.detectMultiScale(grayimg, 1.1, 1)
    for x, y, w, h in car:
        cv2.rectangle(img, (x,y),(x+w, y+h), (255,255,55), 3)
        values = grayimg[y:y+h, x:x+w]
        newcar = cv2.resize(values, (width,height))

    cv2.imshow('...', img)
    key = cv2.waitKey(10)
    if key == 27:
        break