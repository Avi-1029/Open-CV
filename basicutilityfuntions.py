import cv2

mountain = cv2.imread('images//mountains.png',cv2.IMREAD_COLOR)
snowhouse = cv2.imread('images//snowhouse.png',cv2.IMREAD_COLOR)

#resizing images
mountain = cv2.resize(mountain, (600, 400))
cv2.imshow('hi', mountain)
cv2.waitKey(0)
snowhouse = cv2.resize(snowhouse, (600, 400))
cv2.imshow('bye', snowhouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

#adding images

mounthouse = cv2.add(mountain, snowhouse)
cv2.imshow('see you again soon', mounthouse)
cv2.waitKey(0)

#weighted addition

snowtain = cv2.addWeighted(mountain, 0.75, snowhouse, 0.25, 0)
cv2.imshow('no you wont', snowtain)
cv2.waitKey(0)
