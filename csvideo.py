
import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow('img1')
cv2.createTrackbar('A', 'img1', 0, 255, nothing)
cv2.createTrackbar('B', 'img1', 0, 255, nothing)
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    A = cv2.getTrackbarPos('A', 'img1')
    B = cv2.getTrackbarPos('B', 'img1')
    '''color max &min range '''
    lower_blue = np.array([A, 0, 0])
    upper_blue = np.array([B, 143, 143])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img2, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 秀圖
    cv2.imshow('img1', frame)
    # cv2.imshow('img2',img2)
    cv2.imshow('res', res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
