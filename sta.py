import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test17.png')
img1 = cv2.imread('test16.png')

kernel = np.ones((5, 5), np.uint8)  # 卷积核
kernel2 = np.ones((10, 10), np.uint8)  # 卷积核

erosion = cv2.erode(img, kernel, iterations=1)  # 腐蚀
dilation = cv2.dilate(img, kernel, iterations=1)  # 膨胀
# erosion &dilation差值
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)  # 开运算

closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)  # 闭运算
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # 形态学梯度
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)  # 礼帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)  # 黑帽

plt.subplot(241), plt.imshow(img), plt.title('Original')
plt.subplot(242), plt.imshow(erosion), plt.title('Erosion')
plt.subplot(243), plt.imshow(dilation), plt.title('Dilation')
plt.subplot(244), plt.imshow(opening), plt.title('Opening')
plt.subplot(245), plt.imshow(closing), plt.title('Closing')
plt.subplot(246), plt.imshow(gradient), plt.title('Gradient')
plt.subplot(247), plt.imshow(tophat), plt.title('Tophat')
plt.subplot(248), plt.imshow(blackhat), plt.title('Blackhat')

plt.show()
