import cv2
import numpy as np

ghostie = cv2.imread('images/ghost_red.png',cv2.IMREAD_COLOR)
sad_ghostie = cv2.cvtColor(ghostie, cv2.COLOR_BGR2GRAY)
ghostie_blur = cv2.blur(sad_ghostie, (4,8)) #blurring an image

detection = cv2.HoughCircles(ghostie_blur, cv2.HOUGH_GRADIENT, 1, 2, param1= 65, param2= 33, minRadius=0, maxRadius=40)
print(detection) 
print(detection [0])
if detection is not None:
    detection = np.uint(np.around(detection))
    for x, y, r in detection [0]:
        print(x, y, r)
        cv2.circle(ghostie, (x, y), r, (50,0,30), 3) 
        cv2.imshow('...', ghostie)
        cv2.waitKey(0)
    



