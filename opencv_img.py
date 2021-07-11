import numpy as np
import cv2


# print(cv2.__version__)
image = cv2.imread("D:/opencv_images/2.jpg", cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)


## fuctoins
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
img_canny = cv2.Canny(image, 150, 100)
img_dialation = cv2.dilate(img_canny, kernel, iterations = 1)


cv2.imshow("Gray Image", img_gray)
# cv2.imshow("Blur Image", img_blur)
# cv2.imshow("Canny Image", img_canny)
# cv2.imshow("Dialation Image", img_dialation)
cv2.waitKey(0)