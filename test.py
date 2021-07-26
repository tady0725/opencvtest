import cv2
# 開圖
img = cv2.imread('sky.jpg', cv2.IMREAD_GRAYSCALE)
# 秀圖
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow('test', img)

k = cv2.waitKey(0)
if k == 27:  # ESC 退出
    cv2.destroyAllWindows()
elif k == ord('s'):  # 's' 保存退出
    cv2.imwrite('test.jpg', img)
    cv2.destroyAllWindows()
