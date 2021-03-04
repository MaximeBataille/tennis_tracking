import cv2 

def draw_court(img):

	# coordinates found manually
	x_1 = 574
	y_1 = 300

	x_2 = 1338
	y_2 = 300

	x_3 = 1570
	y_3 = 857

	x_4 = 358
	y_4 = 857

	cv2.line(img, (x_1, y_1), (x_2, y_2), (0, 0, 255), 2)
	cv2.line(img, (x_2, y_2), (x_3, y_3), (0, 0, 255), 2)
	cv2.line(img, (x_3, y_3), (x_4, y_4), (0, 0, 255), 2)
	cv2.line(img, (x_4, y_4), (x_1, y_1), (0, 0, 255), 2)

	return img