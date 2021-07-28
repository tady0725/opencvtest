import cv2
import numpy as np
from matplotlib import pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式

img = cv2.imread('test21_3.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 极点
img0 = img.copy()
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
cv2.circle(img0, leftmost, 5, [0, 0, 255], -1)
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
cv2.circle(img0, rightmost, 5, [0, 0, 255], -1)
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
cv2.circle(img0, topmost, 5, [0, 0, 255], -1)
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
cv2.circle(img0, bottommost, 5, [0, 0, 255], -1)
text1 = 'Leftmost: ' + str(leftmost) + ' Rightmost: ' + str(rightmost)
text2 = 'Topmost: ' + str(topmost) + ' Bottommost: ' + str(bottommost)
cv2.putText(img0, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img0, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# 直边界矩形拟合
img1 = img.copy()
x, y, w, h = cv2.boundingRect(cnt)
area = cv2.contourArea(cnt)
aspect_ratio = float(w)/h  # 长宽比
rect_area = w*h
extent = float(area)/rect_area  # 轮廓面积与边界矩形面积的比。
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area  # 轮廓面积与凸包面积的比。
cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)
text1 = 'Aspect Ration: ' + str(round(aspect_ratio, 4))
text2 = 'Extent:  ' + str(round(extent, 4))
text3 = 'Solidity: ' + str(round(solidity, 4))
cv2.putText(img1, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img1, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img1, text3, (10, 90), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# 最小矩形拟合
img2 = img.copy()
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)  # 获得矩形角点
area = cv2.contourArea(box)
width = rect[1][0]
height = rect[1][1]
cv2.polylines(img2, [box], True, (0, 255, 0), 3)
text1 = 'Width: ' + str(int(width)) + ' Height: ' + str(int(height))
text2 = 'Rect Area: ' + str(area)
cv2.putText(img2, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img2, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# 圆拟合
img3 = img.copy()
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
cv2.circle(img3, center, radius, (0, 255, 0), 2)
text1 = 'Center: (' + str(int(x)) + ', ' + str(int(y)) + ') '
text2 = 'Diameter: ' + str(2*radius)
cv2.putText(img3, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img3, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# 椭圆拟合
img4 = img.copy()
ellipse = cv2.fitEllipse(cnt)
(x, y), (a, b), angle = cv2.fitEllipse(cnt)
cv2.ellipse(img4, ellipse, (0, 255, 0), 2)
text1 = 'x: ' + str(int(x)) + ' y: ' + str(int(y))
text2 = 'a:  ' + str(int(a)) + ' b:  ' + str(int(b))
text3 = 'angle: ' + str(round(angle, 2))
cv2.putText(img4, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img4, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img4, text3, (10, 90), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# 直线拟合
img5 = img.copy()
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
slope = -float(vy)/float(vx)  # 直线斜率
lefty = int((x*slope) + y)
righty = int(((x-cols)*slope)+y)
cv2.line(img5, (cols-1, righty), (0, lefty), (0, 255, 0), 2)
text1 = 'Center: (' + str(int(x)) + ', ' + str(int(y)) + ') '
text2 = 'Slope: ' + str(round(slope, 2))
cv2.putText(img5, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img5, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

plt.subplot(231), plt.imshow(cv2.cvtColor(
    img0, cv2.COLOR_BGR2RGB)), plt.title('Pole')
plt.subplot(232), plt.imshow(cv2.cvtColor(
    img1, cv2.COLOR_BGR2RGB)), plt.title('Rectangle')
plt.subplot(233), plt.imshow(cv2.cvtColor(
    img2, cv2.COLOR_BGR2RGB)), plt.title('Rectangle')
plt.subplot(234), plt.imshow(cv2.cvtColor(
    img3, cv2.COLOR_BGR2RGB)), plt.title('Circle')
plt.subplot(235), plt.imshow(cv2.cvtColor(
    img4, cv2.COLOR_BGR2RGB)), plt.title('Ellipse')
plt.subplot(236), plt.imshow(cv2.cvtColor(
    img5, cv2.COLOR_BGR2RGB)), plt.title('Line')
plt.show()
