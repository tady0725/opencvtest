import numpy as np
import cv2 as cv
# 鼠标回调函数
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDBLCLK:
        # cv.circle(img, (x, y), 100, (255, 0, 0), -1)
        cv.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 5)


# 開圖
img = cv.imread('sky.jpg')
# 秀圖
cv.namedWindow('img', cv.WINDOW_NORMAL)
cv.imshow('img', img)

cv.setMouseCallback('img', draw_circle)
while(1):
    cv.imshow('img', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
