import cv2
import numpy as np
from matplotlib import pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式

img1 = cv2.imread('test21_4.jpg')
imgray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('test21_4_1.jpg')
imgray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img3 = cv2.imread('test21_1.jpg')
imgray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(imgray1, 127, 255, 0)
ret, thresh2 = cv2.threshold(imgray2, 127, 255, 0)
ret, thresh3 = cv2.threshold(imgray3, 127, 255, 0)

contours, hierarchy = cv2.findContours(
    thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
contours, hierarchy = cv2.findContours(
    thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours[0]
contours, hierarchy = cv2.findContours(
    thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt3 = contours[0]

match1 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
text = 'Similarity Rate: ' + str(100 - round(match1, 4)*100) + '%'
cv2.putText(img2, text, (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA, 0)

match2 = cv2.matchShapes(cnt1, cnt3, 1, 0.0)
text = 'Similarity Rate: ' + str(100 - round(match2, 4)*100) + '%'
cv2.putText(img3, text, (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA, 0)

plt.subplot(131), plt.imshow(cv2.cvtColor(
    img1, cv2.COLOR_BGR2RGB)), plt.title('Image1')
plt.subplot(132), plt.imshow(cv2.cvtColor(
    img2, cv2.COLOR_BGR2RGB)), plt.title('Image2')
plt.subplot(133), plt.imshow(cv2.cvtColor(
    img3, cv2.COLOR_BGR2RGB)), plt.title('Image3')
plt.show()
