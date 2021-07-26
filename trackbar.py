import cv2
R = 0
G = 0
B = 0
S = 1


def nothing(x):
    global R, G, B, S
    R = cv2.getTrackbarPos('R', 'image')
    G = cv2.getTrackbarPos('G', 'image')
    B = cv2.getTrackbarPos('B', 'image')
    S = cv2.getTrackbarPos('S', 'image')


def drawcircle(event, x, y, flags, param):
    global R, G, B, S
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img1,(x,y),100,(255,0,0),3)
        cv2.rectangle(img1, (x, y), (x+100, y+100), (B, G, R), S)


img1 = cv2.imread('./sky.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', drawcircle)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('S', 'image', 1, 10, nothing)
while(1):
    cv2.imshow('image', img1)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
