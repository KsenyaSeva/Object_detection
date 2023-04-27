import cv2
import numpy as np
import time


capture = cv2.VideoCapture('FullSizeRender.MOV')

#output = cv2.VideoWriter('FullSizeRender.avi', cv2.VideoWriter_fourcc(*'MPEG'), 30, (600, 800))

fl, img1 = capture.read()
fl, img3 = capture.read()

while capture.isOpened():
    diff = cv2.absdiff(img1, img3)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2. threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
       (x, y, w, h) = cv2.boundingRect(contour)

       if cv2.contourArea(contour) < 700:
           continue
       cv2.rectangle(img1, (x, y), (x+w, y+h), (255, 0, 0), 2)
       cv2.putText(img1, 'Detected', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)





    cv2.imshow("Car", img1)
    img1 = img3
    fl, img3 = capture.read()

    if cv2.waitKey(30) == ord('q'):
        break

capture.release()
#output.release()
cv2.destroyAllWindows()





