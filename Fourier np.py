import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./car.jpg', 0)
# 快速傅里叶变换
f = np.fft.fft2(img)
# 将FFT输出中的直流分量移动到频谱的中央
fshift = np.fft.fftshift(f)
# 对数变换
magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
magnitude_spectrum1 = 20*np.log(np.abs(fshift))
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)

plt.subplot(231), plt.imshow(img, cmap='gray'),
plt.title('Input Image'), plt.axis('off')
plt.subplot(232), plt.imshow(magnitude_spectrum, cmap='gray'),
plt.title('Magnitude Spectrum'), plt.axis('off')
plt.subplot(233), plt.imshow(magnitude_spectrum1, cmap='gray'),
plt.title('After High-pass Filtering'), plt.axis('off')
plt.subplot(234), plt.imshow(img, cmap='gray'),
plt.title('Input Image'), plt.axis('off')
plt.subplot(235), plt.imshow(img_back, cmap='gray'),
plt.title('Image after HPF'), plt.axis('off')
plt.subplot(236), plt.imshow(img_back, cmap='jet'),
plt.title('Result in JET'), plt.axis('off')
plt.show()
