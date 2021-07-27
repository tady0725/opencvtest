import cv2
import numpy as np
from matplotlib import pyplot as plt


def bgr2rbg(img):
    '''
        将颜色空间从BGR转换为RBG
    '''
    return img[:, :, ::-1]


# 開圖
img = cv2.imread('./sky.jpg')
cv2.namedWindow('img1')
img1 = cv2.resize(img, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_CUBIC)
img2 = img1[:, ::-1]
img3 = img1[::-1]
img4 = img1[::-1, ::-1]

# 秀圖
plt.subplot(221)
plt.title('SRC')
plt.imshow(bgr2rbg(img1))

plt.subplot(222)
plt.title('Horizontally')
plt.imshow(bgr2rbg(img2))

plt.subplot(223)
plt.title('Vertically')
plt.imshow(bgr2rbg(img3))

plt.subplot(224)
plt.title('Horizontally & Vertically')
plt.imshow(bgr2rbg(img4))

plt.show()
