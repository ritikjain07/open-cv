import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)


# //averaging

avg = cv.blur(img, (7, 7))
cv.imshow('Average Blur', avg)


# //Gaussian blur

gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gaussian)


# //median blur

median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)


# //bilateral blur

bilateral = cv.bilateralFilter(img, 15, 75, 75)
cv.imshow('Bilateral Blur', bilateral)


# //canny edge detection

edges = cv.Canny(img, 100, 200)
cv.imshow('Canny Edges', edges)


# //thresholding

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)



cv.waitKey(0)