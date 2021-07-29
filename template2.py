import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./IMG20201129111424.jpg')
img_rgb = img.copy()
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./test55-1.jpg', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
print(res)
threshold = 0.8

loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)),
plt.title('Original'), plt.axis('off')
plt.subplot(132), plt.imshow(template, cmap='gray'),
plt.title('Template'), plt.axis('off')
plt.subplot(133), plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)),
plt.title('Matching Result'), plt.axis('off')
plt.show()
