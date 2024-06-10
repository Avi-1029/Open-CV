import cv2

eyes = cv2.imread('images//eyes_real.jpg',cv2.IMREAD_COLOR)
sad_eyes = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)

detection = cv2.HoughCircles(sad_eyes, cv2.HOUGH_GRADIENT, 1, 10, param1= 65, param2= 33, minRadius=20, maxRadius=40)
print(detection)

