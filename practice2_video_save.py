import cv2
path = 'C:/Users/seojin/Projects/opencv_study/'

cap = cv2.VideoCapture(0) # 내장 카메라 사용

# 코덱
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 저장할 영상 이름, 프레임 수, 창 크기
writer = cv2.VideoWriter(path + 'output.avi', fourcc, 30.0, (640, 480))

while(True):
    ret, img_color = cap.read() # 카메라로 부터 읽기

    if ret == False:
        continue # 캡쳐가 되지 않은 경우 대해서 필요한 처리

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow('color', img_color) # 저장된 이미지 출력
    cv2.imshow('gray color', img_gray) # grayscale 영상

    writer.write(img_color)

    if cv2.waitKey(1)&0xFF == 27: # ESC를 클릭하면 루프에서 빠져나옴.
        break
#영상은 캡쳐한 이미지를 연속적으로 출력하는 것.

#객체 제한 해제
cap.release()
writer.release()
cv2.destroyAllWindows()