import cv2

pika = cv2.imread('images//pikachu.png',cv2.IMREAD_COLOR)
cv2.imshow('...',pika)
cv2.waitKey(0)

#Drawing A Line

pikawithline = cv2.line(pika, (0, 20), (250, 20), (80,20,60), 3, cv2.LINE_AA)
cv2.imshow('...',pikawithline)
cv2.waitKey(0)

cv2.imshow('...',pika)
cv2.waitKey(0)

#Drawing A Rectangle

cv2.rectangle(pika, (0,20), (400, 120), (60,30,100), 3, cv2.LINE_8)
cv2.imshow('...',pika)
cv2.waitKey(0)

#Drawing a filledrectangle

cv2.rectangle(pika, (0,20), (440, 120), (60,30,100), -1, cv2.LINE_8)
cv2.imshow('...',pika)
cv2.waitKey(0)

#Drawing A Circle

pika = cv2.imread('images//pikachu.png',cv2.IMREAD_COLOR)

r , c = pika.shape [0 : 2]

#cv2.circle(pika, (c//2, r//2), c//2, (50,40,90), 4)
#cv2.imshow('...',pika)
#cv2.waitKey(0)

#Filled Circle

#cv2.circle(pika, (c//2, r//2), c//2, (50,40,90), -4)
#cv2.imshow('...',pika)
#cv2.waitKey(0)

#Text On Image

cv2.putText(pika, "Pikachu is the best and if you say otherwise, youre WRONG!!!", (0, r//4), cv2.FONT_ITALIC, 0.4, (0,0,255), 1)
cv2.imshow('...',pika)
cv2.waitKey(0)
