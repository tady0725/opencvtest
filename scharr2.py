import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./sky.jpg', 0)
scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
scharry = cv.Scharr(img, cv.CV_64F, 0, 1)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

cv.imshow('img', img)
cv.imshow('scharrx', scharrx)
cv.imshow('scharry', scharry)
cv.imshow('scharrxy', scharrxy)
cv.waitKey(0)
cv.destroyAllWindows()
