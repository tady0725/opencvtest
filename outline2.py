import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):  # 滑动条的回调函数
    pass


src = cv2.imread('test21_2.jpg')  # 图片1
imgray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
WindowName = 'Approx'  # 窗口名
cv2.namedWindow(WindowName, cv2.WINDOW_AUTOSIZE)  # 建立空窗口

cv2.createTrackbar('epsilon', WindowName, 0, 10, nothing)  # 两张图片间转换


while(1):
    img = src.copy()
    n = 10 - cv2.getTrackbarPos('epsilon', WindowName)  # 获取a1滑动条值

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    length = cv2.arcLength(cnt, True)

    epsilon = (n/100)*length
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    M = cv2.moments(approx)
    area = cv2.contourArea(approx)
    length1 = cv2.arcLength(approx, True)

    cv2.drawContours(img, approx, -1, (0, 255, 0), 3)
    cv2.polylines(img, [approx], True, (0, 255, 0), 3)

    font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式
    text1 = 'Area:  '+str(int(area))+'  Length:  '+str(int(length1))
    text2 = 'epsilon = ' + str(n) + '%'
    cv2.putText(img, text1, (10, 30), font, 0.5,
                (0, 255, 0), 1, cv2.LINE_AA, 0)
    cv2.putText(img, text2, (10, 60), font, 0.5,
                (0, 255, 0), 1, cv2.LINE_AA, 0)

    cv2.imshow(WindowName, img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
