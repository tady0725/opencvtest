import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./sky.jpg')  # 注意图片尺寸必须是卷积核的整倍，否则出错

# 2D卷积滤波
kernel = np.ones((5, 5), np.float32)/25  # 创建一个5x5的平均滤波器核
dst = cv2.filter2D(img, -1, kernel)

# 平均模糊
blur = cv2.blur(img, (5, 5))

# 高斯滤波
gauss = cv2.GaussianBlur(img, (5, 5), 0)

# 中值滤波
median = cv2.medianBlur(img, 5)

# 双边滤波
bila = cv2.bilateralFilter(img, 10, 200, 200)

plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.subplot(232), plt.imshow(dst), plt.title('Filter2D')
plt.subplot(233), plt.imshow(blur), plt.title('Averaging')
plt.subplot(234), plt.imshow(gauss), plt.title('GuassianBlur')
plt.subplot(235), plt.imshow(median), plt.title('MedianBlur')
plt.subplot(236), plt.imshow(bila), plt.title('BilateralFilter')

plt.show()
