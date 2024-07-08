import cv2
import numpy as np

blobs = cv2.imread('blobs.jpg',cv2.IMREAD_COLOR)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
params.filterByCircularity = True
params.minCircularity = 0.5
params.filterByConvexity = True
params.minConvexity = 0.2
params.filterByInertia = True
params.minInertiaRatio = 0.1
params.maxInertiaRatio = 0.7

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(blobs)
print(keypoints)

result = cv2.drawKeypoints(blobs, keypoints, np.zeros((1,1)), (200, 130, 130), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

lenn = len(keypoints)
cv2.putText(result, str(lenn), (20, 40), cv2.FONT_ITALIC, 1, (0,0,0), 2 )

cv2.imshow('ooo', result)
cv2.waitKey(0)