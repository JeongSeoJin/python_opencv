import cv2

path = 'C:/Users/seojin/Projects/opencv_study/'

img_color = cv2.imread(path + 'test.png', cv2.IMREAD_COLOR) # image파일을 color로 읽어오기 IMREAD_COLOR : flag

# IMREAD_COLOR : alpha 무시, Image파일을 color로 읽음
# IMREAD_GRAYSCALE : grayscale이미지로 읽어옴
# IMREAD_UNCHANGED : alpha와 함께 color로 읽음

cv2.namedWindow('show image')
cv2.imshow('show image', img_color)

cv2.waitKey(0) # 키보드 입력 무한히 대기

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) # grayscale로 변환

cv2.imshow('show gray scale image', img_gray) # 새로운 윈도우에 img_gray를 출력.
cv2.waitKey(0)

cv2.imwrite(path + 'savedimage.png', img_gray)

cv2.destroyAllWindows() # 프로그램 종료 전 윈도우를 위한 자원 해제