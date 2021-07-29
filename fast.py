import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test30.jpg', 0)
# 使用默认值初始化FAST对象
fast = cv2.FastFeatureDetector_create()

# 寻找和画出关键点
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))

# 关闭非最大值抑制
fast.setNonmaxSuppression(False)
kp = fast.detect(img, None)

img3 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.subplot(121), plt.imshow(img2),
plt.title('开启非极大值抑制'), plt.axis('off')
plt.subplot(122), plt.imshow(img3),
plt.title('关闭非极大值抑制'), plt.axis('off')
plt.show()
