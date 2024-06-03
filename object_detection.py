import cv2

ghostie = cv2.imread('images/ghost_red.png',cv2.IMREAD_COLOR)
sad_ghostie = cv2.cvtColor(ghostie, cv2.COLOR_BGR2GRAY)
ghostie_blur = cv2.blur(sad_ghostie, (4,8)) #blurring an image

detection = cv2.HoughCircles(ghostie_blur, cv2.HOUGH_GRADIENT, 1, 10, param1= 65, param2= 33, minRadius=20, maxRadius=40)
print(detection) 
print(detection [0])
if detection is not None:
    for x, y, r in detection [0]:
        print(x, y, r) 
    



