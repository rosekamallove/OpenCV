import cv2
import random

img = cv2.imread('tiger.jpg', -1)

#Copying and Pasting part of an image:

part = img[500:700, 600:900] #numPyArraySlice: I wanna copy from row 500 -> 700 and in those rows i wanna copy coloumns 600 -> 900 

#the dimesions of the place i wanna copy to has to be same as the dimesions of the part i copied
img[100:300, 650:950] = part
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
