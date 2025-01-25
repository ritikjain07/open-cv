import cv2 as cv
import numpy as np

image = cv.imread('Photos/lady.jpg')

cv.imshow('Lady', image)

# Translation
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)

translate = translate(image, -100, 100)
# cv.imshow('Translation', translate)

# Rotation

def rotate(img, angle, center=None):
    (height, width) = img.shape[:2]
    if center is None:
        center = (width // 2, height // 2)
    rot_mat = cv.getRotationMatrix2D(center, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rot_mat, dimensions)

rotated = rotate(image, -45)

# cv.imshow('Rotation', rotated)


# Resizing

resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)

# cv.imshow('Resized', resized)


# Flipping

flip = cv.flip(resized, 0)

cv.imshow('Flip', flip)
        
cv.waitKey(0)