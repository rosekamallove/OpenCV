import numpy as np
import cv2

cap = cv2.VideoCapture(0) #change 0 to filename if wanna import file

while True:
    ret, frame = cap.read() #Returns the frame which is the image itself
    width=int(cap.get(3))
    height=int(cap.get(4))
    # creating four coordants of you beutiful face

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    ##now what we are going to do is rotate the videos in different directions
    image[:height//2, :width//2]=cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2]=smaller_frame
    image[:height//2, width//2:]=cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:]=smaller_frame


    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): #if within 1 milisecond the key that is pressed is q then break
        break

cap.release()
cv2.destroyAllWindows()
