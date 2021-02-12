import cv2
import random

img = cv2.imread('tiger.jpg', 1)

#Accesing Pixel Values

#Printing the first row of the image:
print(img[0]) #img at index 0
print(img[257][45:400])#this prints a lot of 0s well because the image has a lot of balck pixels

#Changing Pixel Colors

for i in range(100):
    for j in range(img.shape[1]):#img.shape gives us: (rows, coloumns, channels)
        img[i][j] = [random.randrange(255), random.randrange(255),random.randrange(255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


