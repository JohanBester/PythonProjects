import cv2

cv2.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv2.CaptureFromCAM(camera_index)

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    frame = cv2.QueryFrame(capture)
    cv2.ShowImage("w1", frame)
    c = cv2.WaitKey(10)
    if(c=="n"): #in "n" key is pressed while the popup window is in focus
        camera_index += 1 #try the next camera index
        capture = cv2.CaptureFromCAM(camera_index)
        if not capture: #if the next camera index didn't work, reset to 0.
            camera_index = 0
            capture = cv2.CaptureFromCAM(camera_index)

while True:
    repeat()
