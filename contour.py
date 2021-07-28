import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./sky.jpg')
cv2.namedWindow('image')
blur = cv2.GaussianBlur(img, (9, 9), 0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
scharrx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
scharry = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
edges1 = cv2.Canny(scharrxy, 50, 200)


contours, hi = cv2.findContours(edges1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img1 = edges1
newcountours = []
for contour in contours:
    if cv2.contourArea(contour) > 600 and cv2.arcLength(contour, True) < 200:
        newcountours.append(contour)
cv2.drawContours(img, newcountours, -1, (0, 255, 0), 2)

print(len(contours), len(newcountours))
for a in newcountours:
    print(cv2.arcLength(a, True), cv2.contourArea(a))
# print(cv2.moments(newcountours[-1]))
# print(cv2.contourArea(contours[100]))
cv2.imshow('edg', edges1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
