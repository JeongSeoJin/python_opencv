import cv2

def nothing(x):
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)

path = 'C:/Users/seojin/Projects/opencv_study/'

img_color = cv2.imread(path + 'image.jpg', cv2.IMREAD_COLOR) #컬러 이미지로 불러오기

img_resize = cv2.resize(img_color, (400, 550))
cv2.imshow("color image", img_resize)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray scale image', img_gray)
cv2.waitKey(0)

while(True):
    low = cv2.getTrackbarPos('threshold', 'Binary')
#                                        임계값,      255, 0 중 어느 값을 부여할지 결정
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)

    cv2.imshow('Binary', img_binary)

    img_result = cv2.bitwise_and(img_resize, img_resize, mask = img_binary)
    cv2.imshow('result', img_result )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()