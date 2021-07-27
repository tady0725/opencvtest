import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

kernel = np.ones((5, 5), np.uint8)
img = cv.imread('./sky.jpg', 0)
ret3, th3 = cv.threshold(img, 0, 255, cv.THRESH_TOZERO+cv.THRESH_OTSU)
erosion = cv.erode(th3, kernel, iterations=1)
dilation = cv.dilate(th3, kernel, iterations=1)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# roi = th3[200:400,400:800]
# gauss = cv.GaussianBlur(roi, (11, 11), 3)
# th3[200:400,400:800]=gauss
cv.imshow('img', img)
cv.imshow('th3', th3)
cv.imshow('gauss', erosion)
cv.imshow('dilation', dilation)
cv.imshow('gradient', gradient)
cv.waitKey(0)
cv.destroyAllWindows()
