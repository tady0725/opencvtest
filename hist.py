import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./sky.jpg')
img1 = cv.imread('./sky.jpg', 0)
color = ('b', 'g', 'r')
# for i, col in enumerate(color):
#     histr = cv.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 256])
histr = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.xlim([0, 256])

plt.show()
