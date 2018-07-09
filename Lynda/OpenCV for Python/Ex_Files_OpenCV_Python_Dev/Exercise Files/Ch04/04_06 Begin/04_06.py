import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=1,fy=1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	path = "haarcascade_eye.xml"

	face_cascade = cv2.CascadeClassifier(path)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=5, minSize=(40, 40))

	for (x, y, w, h,) in faces:
		cv2.circle(frame, ((x+int((0.5 * w))), y+int((0.5 * h))), int(w/2), (0,255,0), 2)

	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()