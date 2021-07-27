import cv2 as cv

# 加载两张图片
img1 = cv.imread('./sky.jpg')
img2 = cv.imread('./logo.jpeg')
# 我想在左上角放置一个logo，所以我创建了一个 ROI,并且这个ROI的宽和高为我想放置的logo的宽和高
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# 现在创建一个logo的掩码，通过对logo图像进行阈值，并对阈值结果并创建其反转掩码
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 180, 220, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# 现在使 ROI 中的徽标区域变黑
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
# 仅从徽标图像中获取徽标区域。
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
# 在 ROI 中放置徽标并修改主图像
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
# cv.imshow('img2gray', img2gray)
# cv.imshow('mask', mask)
# cv.imshow('mask_inv', mask_inv)
# cv.imshow('img1_bg', img1_bg)
# cv.imshow('img2_fg', img2_fg)
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()
