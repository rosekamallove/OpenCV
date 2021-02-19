import numpy as np
import cv2

cap = cv2.VideoCapture(0) #change 0 to filename if wanna import file

while True:
    ret, frame = cap.read() #Returns the frame which is the image itself

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #if within 1 milisecond the key that is pressed is q then break
        break

cap.release()
cv2.destroyAllWindows()
