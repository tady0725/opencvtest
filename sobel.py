import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./sky.jpg', 0)
sobel = cv.Sobel(img, cv.CV_8U, 1, 1, ksize=3)
sobelx = cv.Sobel(img, cv.CV_32F, 1, 0, ksize=3)
sobely = cv.Sobel(img, cv.CV_32F, 0, 1, ksize=3)
sobel2 = cv.Sobel(img, cv.CV_8U, 1, 1, ksize=5)
cv.imshow('img', img)
cv.imshow('sobel3', sobel)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('sobel5', sobel2)
cv.waitKey(0)
cv.destroyAllWindows()
