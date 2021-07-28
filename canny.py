import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('./sky.jpg')
img1 = cv2.imread('./sky.jpg', 0)
cv2.namedWindow('image')
cv2.createTrackbar('min', 'image', 0, 255, nothing)
cv2.createTrackbar('max', 'image', 0, 255, nothing)
cv2.imshow('image', img)
blur = cv2.GaussianBlur(img, (9, 9), 0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
scharrx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
scharry = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

while(True):
    min = cv2.getTrackbarPos('min', 'image')
    max = cv2.getTrackbarPos('max', 'image')
    # edges = cv2.Canny(img, min, max)
    edges = cv2.Canny(scharrxy, min, max)
    edges1 = cv2.Canny(img1, min, max)
    edges2 = cv2.bitwise_and(img, img, mask=edges)
    cv2.imshow('canny1', edges)
    cv2.imshow('canny2', edges1)
    cv2.imshow('edge2', edges2)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
