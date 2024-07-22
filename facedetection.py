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

imgcount = 0

while imgcount<30:
    r, i = video.read()
    sadimg = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    face = facedet.detectMultiScale(sadimg, 1.3, 5)
    if face is not None:
        imgcount = imgcount + 1
    for x, y, w, h in face:
        cv2.rectangle(i, (x,y),(x+w, y+h), (255,255,255), 3)
        values = sadimg[y:y+h, x:x+w]
        newface = cv2.resize(values, (width,height))
        cv2.imwrite(path + '\\' + subfolder + str(imgcount) + '.png', newface )
    cv2.imshow('...', i)   
    key = cv2.waitKey(100)
    if key == 27:
        break








