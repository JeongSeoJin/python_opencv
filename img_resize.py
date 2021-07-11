import numpy as np
import cv2


# print(cv2.__version__)
img = cv2.imread("D:/my_files/my_image.jpg", cv2.IMREAD_UNCHANGED)

img_resize = cv2.resize(img, (600, 337))

cv2.imshow("Image", img)
print(img_resize.shape)

cv2.imshow("resized Image", img_resize)

cv2.waitKey(0)