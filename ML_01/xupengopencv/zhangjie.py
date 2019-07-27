import cv2
import time

def live_classifier():
    #打开摄像头
    cap = cv2.VideoCapture(0)
    #加载脸，眼睛，笑容的级联分类器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    n=1;
    while(True):
        #读取摄像头画面      画面为frame
        ret,frame = cap.read()
        img = frame
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        #对联进行检测
        faces = face_cascade.detectMultiScale(img, 1.2, 2)

        for (fx,fy,fw,fh) in faces:
            #画出脸的位置
            img = cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (0, 200, 200), 2)
            #截取脸的位置，在此位置上进行眼睛检测
            face_area = img[fy:fy + fh, fx:fx + fw]
            # cv2.imwrite('xu.png',face_area)
            eyes = eye_cascade.detectMultiScale(face_area, 1.2,10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face_area, (ex, ey), (ex + ew, ex + eh), (0, 255, 0), 1)
            smiles = smile.detectMultiScale(face_area, 1.2, 10)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(face_area, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 1)
                cv2.putText(img, 'Smile', (fx, fy - 7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
            img1 = img[fy:fy+fh,fx:fx+fw]
            cv2.imwrite(str(n)+'pbxd.png',img1)
            n=n+1
        #显示出检测后的画面
        cv2.imshow('xupeng',img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        # time.sleep(1)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    live_classifier()