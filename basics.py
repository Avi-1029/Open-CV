import cv2

#reading and displaying images
pika = cv2.imread('images\\pikachu.png',cv2.IMREAD_COLOR) #To read the image
cv2.imshow('Image',pika) #Show the image
cv2.waitKey(0) #Make the image stay on the screen (0 means it will stay till I press any other key)
#cv2.destroyAllWindows() Closes all windows

#Read and display an image in gray scale
pika_gray = cv2.imread('images\\pikachu.png',cv2.IMREAD_GRAYSCALE) #Turns the image gray
cv2.imshow('.',pika_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Saving and image
cv2.imwrite('images\\pika_gray.png',pika_gray) 