import cv2
import numpy as np
from matplotlib import pyplot as plt


def plot(img, n):
    filename = img
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    # 输入图像必须是 float32，最后一个参数在 0.04 到 0.05 之间
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.005*dst.max()] = [255, 0, 0]
    plt.subplot(1, 3, n), plt.imshow(img, cmap='gray'),
    plt.title('dst'), plt.axis('off')


plot('test30.jpg', 1)
plot('test30_1.jpg', 2)
plot('test30_2.jpg', 3)

plt.show()
