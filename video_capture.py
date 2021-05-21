import cv2

cap = cv2.VideoCapture('D:/my_files/hangmangame.mp4')

while(cap.isOpened()):
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()