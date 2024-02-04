## [imports]
import cv2 as cv
import sys

## [imread]
img = cv.imread(cv.samples.findFile("starry_night.jpg"))
    
## [empty]
if img is None:
    sys.exit("Could not read the image.")

## [imshow]
cv.imshow("Display window", img)
k = cv.waitKey(0)

## [imsave]
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
