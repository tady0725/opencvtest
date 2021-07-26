import numpy as np
import cv2 as cv
# 创建一个黑色的图像
img = cv.imread('./sky.jpg')
# 画一条 5px 宽的蓝色对角线

cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (100, 0), (200, 128), (0, 255, 0), 5)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv.putText(img, 'hihi', (600, 100), 5, 5, (255, 255, 0))

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))
cv.namedWindow('test', cv.WINDOW_NORMAL)
cv.imshow('test', img)
k = cv.waitKey(0)
if k == 27:  # ESC 退出
    cv.destroyAllWindows()
