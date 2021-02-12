import cv2

# Copying one part of the image to another part of the image

img = cv2.imread('tiger.jpg', -1)

#image representation.
print(img)#this prints out the numpy array of the image, and array is how an image is store
# what it does is it extract the pixels of the  image and puts the into the numpy array.

print(type(img))#prints out class numpy nd array
print(img.shape)#prints out (856,1590,3) (nRows, nColoumns, nChannels) channel is just the color space of our image, RGB etc Note: OpenCV uses BGR
                #the array here is 3Dimensinal 

''' 
Here's an example:
   
    [
    [[0,0,0],[255,255,545]],
    [],
    []
    ] 

    If we had an image of just two pixels it will be layed out like this:
    [
    [[0,0,0],[255,255,545]],
    [[0,0,0],[255,255,545]]
    ]
'''

