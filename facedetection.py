import cv2
import os

mainfolder = "database"
subfolder = "Avi"
path = os.path.join(mainfolder, subfolder)
if not os.path.isdir(path):
    os.makedirs(path)
    
width = 100
height = 130

xmlfile = "haarcascade_frontalface_default.xml"

facedet = cv2.CascadeClassifier(xmlfile)
video = cv2.VideoCapture(0)

for x in range(30):
    r, i = video.read()
    sadimg = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    face = facedet.detectMultiScale(sadimg, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(i, (x,y),(x+w, y+h), (255,255,255), 3)
    cv2.imshow('...', i)   
    key = cv2.waitKey(1000)
    if key == 27:
        break

