import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255

colorOne = (0,255,0)
colorTwo = (0,0,255)
line_width = 3
radius = 100
pointOne = (0,0)
pointTwo = (0,0)

# click callback
def click(event, x, y, flags, param):
	global canvas, pointOne, pointTwo
	if event == cv2.EVENT_LBUTTONDOWN:
		print("LButton Down")
		pointOne = (x,y)
	elif event == cv2.EVENT_RBUTTONDOWN:
		print("RButton Down")
		pointTwo = (x, y)

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)
	cv2.circle(canvas, pointOne, radius, colorOne, line_width)
	cv2.circle(canvas, pointTwo, radius, colorTwo, line_width)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	

cv2.destroyAllWindows()