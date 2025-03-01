import cv2 as cv

#reading the image file

# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)








#reading the vedio file
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
    
# capture.release()
# cv.destroyAllWindows()






