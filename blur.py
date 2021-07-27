import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./car.jpg', 0)
a = img.shape
print(a)
ret3, th3 = cv.threshold(img, 0, 255, cv.THRESH_TOZERO+cv.THRESH_OTSU)
roi = th3[300:500, 200:600]
gauss = cv.GaussianBlur(roi, (11, 11), 5)
th3[300:500, 200:600] = gauss
# cv.imshow('img', img)
cv.imshow('th3', th3)
cv.imshow('gauss', gauss)
cv.waitKey(0)
cv.destroyAllWindows()
