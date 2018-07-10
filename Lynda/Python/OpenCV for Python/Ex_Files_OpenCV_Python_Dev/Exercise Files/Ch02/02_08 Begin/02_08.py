import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    # M = cv2.getRotationMatrix2D((0, 0), -30, 1)

    frame = cv2.resize(frame, (0,0), fx=0.75, fy=0.75)
    cv2.imshow("Frame", frame)

    # rotated = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))
    # cv2.imshow("Rotated", rotated)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()