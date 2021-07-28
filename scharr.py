import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./sky.jpg', 0)
scharrx = cv.Scharr(img, cv.CV_8U, 1, 0)
scharry = cv.Scharr(img, cv.CV_8U, 0, 1)
scharr = cv.Scharr(img, cv.CV_8U, 0, 1)

cv.imshow('img', img)
cv.imshow('scharrx', scharrx)
cv.imshow('scharry', scharry)
cv.imshow('scharr', scharr)
cv.waitKey(0)
cv.destroyAllWindows()
