import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('./sky.jpg', 0)
# 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])

mask = np.zeros(img1.shape[:2], np.uint8)
mask[100:600, 400:800] = 255
masked_img = cv2.bitwise_and(img1, img1, mask=mask)
hist_full = cv2.calcHist([masked_img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img1], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Image1')
plt.subplot(222), plt.plot(hist1), plt.title('Histogram'), plt.xlim([0, 256])
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('Image2')
plt.subplot(224), plt.plot(hist_full), plt.plot(
    hist_mask), plt.title('Histogram'), plt.xlim([0, 256])
plt.show()
