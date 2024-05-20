import cv2
import numpy as np

pikachu = cv2.imread('images//pikachu.png',cv2.IMREAD_COLOR)
#cv2.imshow('hi',pikachu)
#cv2.waitKey(0)

#erosion

weirdpika = cv2.erode(pikachu, np.ones((6,9)))
cv2.imshow('hola',weirdpika)
cv2.waitKey(0)

#putting borders on the image

borderedpika = cv2.copyMakeBorder(pikachu, 12, 10, 12, 10, cv2.BORDER_CONSTANT, value = (50, 30, 60))
cv2.imshow('aloha',borderedpika)
cv2.waitKey(0)

borderedpika1 = cv2.copyMakeBorder(pikachu, 12, 10, 12, 10, cv2.BORDER_REFLECT, value = (50, 30, 60))
cv2.imshow('bonjour',borderedpika1)
cv2.waitKey(0)

#edge detection

Pikawithedge = cv2.Canny(pikachu, 68, 136)
cv2.imshow('cool',Pikawithedge)
cv2.waitKey(0)

mountain = cv2.imread('images//mountains.png', cv2.IMREAD_COLOR)

Mountainwithedge = cv2.Canny(mountain, 68,136)
cv2.imshow('swagger', Mountainwithedge)
cv2.waitKey(0)

#Rotatating and image

r , c = pikachu.shape [0 : 2]

Matrix = cv2.getRotationMatrix2D((c/2 , r/2), 90, 1)
M= cv2.warpAffine(pikachu, Matrix, (r, c))
cv2.imshow('hello',M)
cv2.waitKey(0)