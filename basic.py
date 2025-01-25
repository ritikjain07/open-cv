import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray_Cat', gray)

# Blur
blurred = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('Blurred_Cat', blurred)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny_Cat', canny)

canny = cv.Canny(blurred, 125, 175)
# cv.imshow('Canny_Cat_blurred', canny)


# Dilating the img

dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilating_Cat', dilated)


# Eroding

eroded = cv.erode(dilated, (3,3), iterations=3)
# cv.imshow('Eroding_Cat', eroded)


# resize

resized = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv.imshow('Resized_Cat', resized)



# Cropping
cropped = img[50:200, 200:400]

cv.imshow('Cropped_Cat', cropped)


cv.waitKey(0)
