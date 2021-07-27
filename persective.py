import cv2
import numpy as np
from matplotlib import pyplot as plt
# 抓取四個點 np[x,y]
pts1 = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])
i = 0


def savexy(event, x, y, flags, param):
    global pts1
    global i
    # 左键放开
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, y)
        # Color is by default black
        cv2.circle(img, ((x, y)), 3, (0, 255, 0), 3)
        pts1[i] = [x, y]
        i += 1


img = cv2.imread('./car.jpg')
rows, cols, ch = img.shape
# 左上 ->右上 ->右下 ->左下
pts2 = np.float32([[0, 0], [400, 0], [400, 200], [0, 200]])
cv2.namedWindow('image')

cv2.setMouseCallback('image', savexy)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27 or i > 3:

        break
cv2.destroyAllWindows()
# 投影映射
M = cv2.getPerspectiveTransform(pts1, pts2)
# 透视变换
dst = cv2.warpPerspective(img, M, (400, 200))
# 轉換顏色
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst1 = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img1), plt.title('Input')
plt.subplot(122), plt.imshow(dst1), plt.title('Output')
plt.show()
