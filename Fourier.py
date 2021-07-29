import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./car.jpg', 0)
# 傅里叶变换
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
# 移频
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * \
    np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
# 创建一个掩膜，中间方形为1，其余为0
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# 使用掩膜
fshift = dft_shift*mask
magnitude_spectrum1 = 20 * \
    np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
# 逆移频
f_ishift = np.fft.ifftshift(fshift)
# 逆傅里叶变换
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(221), plt.imshow(img, cmap='gray'),
plt.title('Input Image'), plt.axis('off')
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray'),
plt.title('Magnitude Spectrum')
plt.subplot(223), plt.imshow(img_back, cmap='gray'),
plt.title('Input Image'), plt.axis('off')
plt.subplot(224), plt.imshow(magnitude_spectrum1, cmap='gray'),
plt.title('Magnitude Spectrum')
plt.show()
