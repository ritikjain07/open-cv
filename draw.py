import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Black', blank)

# blank[:] = 0,0,255
# cv.imshow('Red', blank)

# blank[:] = 0,255,255
# cv.imshow('yellow', blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)


# draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0,250,0), thickness=-1)
# cv.imshow('Rectangle', blank)


# draw a circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)


# draw a line

cv.line(blank, (100, 0), (blank.shape[1], blank.shape[0]), (255,0,0), thickness=5)
# cv.imshow('Line', blank)


# text on the image

cv.putText(blank, 'Hello, OpenCV!', (100, 200), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)
cv.imshow('Text', blank)

cv.imwrite('output.png', blank)

# write text

cv.waitKey(0)