import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('test37_0.jpg', 0)
img2 = cv2.imread('test37_1.jpg', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

# 根据距离排序
matches = sorted(matches, key=lambda x: x.distance)

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   flags=0)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, **draw_params)

plt.imshow(img3, cmap='gray'), plt.title('Matched Result'), plt.axis('off')
plt.show()
