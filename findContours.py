import cv2
import numpy as np
from matplotlib import pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式

img = cv2.imread('test21_4.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)

inside = (190, 190)
outside = (50, 50)

img0 = img.copy()
dist1 = cv2.pointPolygonTest(cnt, outside, True)
cv2.circle(img0, outside, 5, [255, 255, 0], -1)
text = 'Point Ploygon Test: ' + str(round(dist1, 2))
cv2.putText(img0, text, (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA, 0)

img1 = img.copy()
dist2 = cv2.pointPolygonTest(cnt, inside, True)
cv2.circle(img1, inside, 5, [255, 255, 0], -1)
text = 'Point Ploygon Test: ' + str(round(dist2, 2))
cv2.putText(img1, text, (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA, 0)

img2 = img.copy()
dist3 = cv2.pointPolygonTest(cnt, outside, False)
cv2.circle(img2, outside, 5, [255, 255, 0], -1)
text = 'Point Ploygon Test: ' + str(dist3)
cv2.putText(img2, text, (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA, 0)

img3 = img.copy()
dist4 = cv2.pointPolygonTest(cnt, inside, False)
cv2.circle(img3, inside, 5, [255, 255, 0], -1)
text = 'Point Ploygon Test: ' + str(dist4)
cv2.putText(img3, text, (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA, 0)

plt.subplot(221), plt.imshow(cv2.cvtColor(
    img0, cv2.COLOR_BGR2RGB)), plt.title('Out & True')
plt.subplot(222), plt.imshow(cv2.cvtColor(
    img1, cv2.COLOR_BGR2RGB)), plt.title('In & True')
plt.subplot(223), plt.imshow(cv2.cvtColor(
    img2, cv2.COLOR_BGR2RGB)), plt.title('Out & False')
plt.subplot(224), plt.imshow(cv2.cvtColor(
    img3, cv2.COLOR_BGR2RGB)), plt.title('In & False')
plt.show()
