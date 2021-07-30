# 辨識照片 呼叫自己修改檔案
from cvzone1 import FaceDetector
import cv2

# cap = cv2.VideoCapture(1)

detector = FaceDetector(model_selection=0)

while True:
    img = cv2.imread('./akb.jpg')
    # success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()
