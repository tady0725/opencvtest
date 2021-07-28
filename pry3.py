import cv2
import numpy as np

img = cv2.imread('./logo.jpeg')
G0 = img
gg = G0.shape
print(gg)
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)
# laplace = cv2.subtract(img, higher1)

cv2.imshow('L0', L0)
cv2.imshow('L1', L1)
cv2.imshow('L2', L2)
cv2.waitKey(0)
cv2.destroyAllWindows()
