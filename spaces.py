import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('Grayscale', gray)

# BGR TO HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# cv.imshow('HSV', hsv)


# BGR TO LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# cv.imshow('LAB', lab)

# BGR TO RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('RGB', rgb)  


cv.waitKey(0)