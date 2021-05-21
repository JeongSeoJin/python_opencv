import numpy as np
import cv2

# print(cv2.__version__)
image = cv2.imread("D:/my_files/TT.jpg")
cv2.imshow("Moon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()