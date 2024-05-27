import cv2
import numpy as np

ss = cv2.imread('images\\subwaysurfers.png',cv2.IMREAD_COLOR) 
cv2.imshow('Image',ss) 
cv2.waitKey(0)

ss_gray = cv2.imread('images\\subwaysurfers.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('.', ss_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images\\ss_gray.png',ss_gray) 

weirdss = cv2.erode(ss, np.ones((6,9)))
cv2.imshow('...',weirdss)
cv2.waitKey(0)

borderedss = cv2.copyMakeBorder(ss, 12, 10, 12, 10, cv2.BORDER_CONSTANT, value = (50, 30, 60))
cv2.imshow('...',borderedss)
cv2.waitKey(0)

sswithedge = cv2.Canny(ss, 68, 136)
cv2.imshow('...', sswithedge)
cv2.waitKey(0)