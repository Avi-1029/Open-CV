import cv2
import numpy as np

lbred = np.array((160, 60, 60))
ubred = np.array((180, 255, 255))
video = cv2.VideoCapture('video.mp4')

for f in range(60):
    r, bg = video.read()
    if r == False:
        continue

while video.isOpened():
    r, f = video.read()
    if r == False:
        break 
    hsvf = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsvf , lbred, ubred)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((7,7)), iterations= 2)
    mask2 = cv2.bitwise_not(mask1)

    r1 = cv2.bitwise_and(bg, bg, mask= mask1)
    r2 = cv2.bitwise_and(f, f, mask= mask2)
    r = cv2.add(r1, r2)

    cv2.imshow('...',r)
    key = cv2.waitKey(10)
    if key == 27:
        break



