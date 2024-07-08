import cv2
import os 
from PIL import Image as im

path = "C:\\Users\\Biju\\Desktop\\Jetlearn\\Open CV\\Images"
os.chdir(path)
numofimg = 0
totalwidth = 0
totalheight = 0 

images = []
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
       images.append(file)
       numofimg = numofimg + 1
       image = im.open(os.path.join(path,file))
       w, h = image.size
       totalwidth = totalwidth + w
       totalheight = totalheight + h 
avw = totalwidth // numofimg
avh = totalheight // numofimg
print(avw, avh) #Calculating the average size of all the images

for file in images:
    image = im.open(os.path.join(path,file))
    newimg = image.resize((1600, 1200)) 
    newimg.save(file, 'JPEG')

videoname = 'verycoolvideo.avi'
video = cv2.VideoWriter(videoname, 0, 1, (avw, avh))

for file in images:
    img = cv2.imread(os.path.join(path,file))
    video.write(img)


