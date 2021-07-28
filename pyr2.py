import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像尺寸最好是2的整次幂，如256,512等
# 否则在金字塔向上的过程中图像的尺寸会不等
# 这会导致在拉普拉斯金字塔处理时由于不同尺寸矩阵相减而出错
img = cv2.imread('./sky.jpg')
lower = cv2.pyrDown(img)
lower1 = cv2.pyrDown(lower)
higher = cv2.pyrUp(lower1)
higher1 = cv2.pyrUp(higher)
laplace = cv2.subtract(img, higher1)

plt.subplot(121), plt.imshow(cv2.cvtColor(
    img, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(
    laplace, cv2.COLOR_BGR2RGB)), plt.title('Laplace')
plt.show()
