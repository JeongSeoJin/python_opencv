import cv2
path = 'C:/Users/seojin/Projects/opencv_study/'

cap = cv2.VideoCapture(path + 'output.avi') # 저장된 영상 출력

# 코덱
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 저장할 영상 이름, 프레임 수, 창 크기
fps = cap.get(cv2.CAP_PROP_FPS)

delay = int(1000 / fps) if fps != 0 else 33  # fps가 0이면 기본값을 33ms로

while(True):
    ret, img_color = cap.read() # 카메라로 부터 읽기

    if ret == False:
        break # 영상이 끝까지 출력되면 루프에서 빠져나도록 수정

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow('color', img_color) # 저장된 이미지 출력
    cv2.imshow('gray color', img_gray) # grayscale 영상
 
    if cv2.waitKey(1) & 0xFF == 27:  # ESC를 누르면 종료
        break
#영상은 캡쳐한 이미지를 연속적으로 출력하는 것.

#객체 제한 해제
cap.release()
cv2.destroyAllWindows()