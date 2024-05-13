import cv2

subwaysurfers = cv2.imread('images\\subwaysurfers.png',cv2.IMREAD_COLOR) 
cv2.imshow('Image',subwaysurfers) 
cv2.waitKey(0)

ss_gray = cv2.imread('images\\subwaysurfers.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('.', ss_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images\\ss_gray.png',ss_gray) 
