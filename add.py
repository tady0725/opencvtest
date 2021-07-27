import cv2

# 開圖
img1 = cv2.imread('./sky.jpg')

print(img1.shape)

# img1[200:400,300:700]=[255,0,0]
roi = img1[300:600, 300:700]
roi2 = img1[100:400, 600:1000]
dst = cv2.addWeighted(roi, 0.7, roi2, 0.3, 0)
img1[100:400, 600:1000] = dst

# 秀圖
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow('test', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
