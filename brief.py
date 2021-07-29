import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test30.jpg', 0)
plt.subplot(131), plt.imshow(img, cmap='gray'),
plt.title('Origianl'), plt.axis('off')

# STAR检测器
star = cv2.xfeatures2d.StarDetector_create()
# BRIEF抽取器
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
# find the keypoints with STAR
kp = star.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
plt.subplot(132), plt.imshow(img2, cmap='gray'),
plt.title('STAR'), plt.axis('off')

# 使用BRIEF计算描述符
kp1, des = brief.compute(img, kp)
img3 = cv2.drawKeypoints(img, kp1, None, color=(255, 0, 0))
plt.subplot(133), plt.imshow(img3, cmap='gray'),
plt.title('BRIEF'), plt.axis('off')
plt.show()

# 打印BRIEF尺寸
print(brief.descriptorSize())
# 打印计算后输出符的尺寸
print(des.shape)
