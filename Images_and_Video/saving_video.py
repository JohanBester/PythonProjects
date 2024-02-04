import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # flip the frame image
    # frame = cv.flip(frame, 0)
    
    # write the flipped frame
    out.write(frame)
    cv.imshow('PRESS Q TO QUITE VIDEO FRAME', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
    
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
