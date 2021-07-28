import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像尺寸最好是2的整次幂，如256,512等
# 否则在金字塔向上的过程中图像的尺寸会不等
# 这会导致在拉普拉斯金字塔处理时由于不同尺寸矩阵相减而出错
A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

# 将苹果进行高斯金字塔处理，总共六级处理
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# 将橘子进行高斯金字塔处理，总共六级处理
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# 将苹果进行拉普拉斯金字塔处理，总共5级处理
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

# 将橘子进行拉普拉斯金字塔处理，总共5级处理
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)

# 将两个图像的矩阵的左半部分和右半部分拼接到一起
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols//2], lb[:, cols//2:]))
    LS.append(ls)

# 采用金字塔拼接方法的图像
ls_ = LS[0]  # 这里LS[0]为高斯金字塔的最小图片
for i in range(1, 6):  # 第一次循环的图像为高斯金字塔的最小图片，依次通过拉普拉斯金字塔恢复到大图像
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# 直接拼接
real = np.hstack((A[:, :cols//2], B[:, cols//2:]))

plt.subplot(221), plt.imshow(cv2.cvtColor(
    A, cv2.COLOR_BGR2RGB)), plt.title('Apple')
plt.subplot(222), plt.imshow(cv2.cvtColor(
    B, cv2.COLOR_BGR2RGB)), plt.title('Orange')
plt.subplot(223), plt.imshow(cv2.cvtColor(
    real, cv2.COLOR_BGR2RGB)), plt.title('Direct')
plt.subplot(224), plt.imshow(cv2.cvtColor(
    ls_, cv2.COLOR_BGR2RGB)), plt.title('Pyramid')
plt.show()
