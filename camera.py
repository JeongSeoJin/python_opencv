import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(20, 200)

p_time = 0

if cap.isOpened():
    while True:
        success, img = cap.read()
        if success:

            c_time = time.time()
            fps = 1/(c_time-p_time)
            p_time = c_time

            cv2.putText(img, f'FPS : {int(fps)}', (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 3)

            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
else:
    print('cannot open the file')
 
cap.release()
cap.destroyAllWindows()