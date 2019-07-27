import cv2

cap = cv2.VideoCapture('C:/Users/16276/Desktop/aaa.mp4')

print(cap.isOpened())
cap.open(0)
while True:
    ret,frame = cap.read()
    print(ret)

    cv2.imshow('d',frame)
    if cv2.waitKey(5)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()