import numpy as np
import cv2

# print(cv2.__version__)
image = cv2.imread("D:/opencv_images/2.jpg")
cv2.imshow("fus", image)
cv2.waitKey(0)
cv2.destroyAllWindows()