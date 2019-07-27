#导入opencv
import cv2
import time
def face():
    #读入一张图片
    img = cv2.imread(r'C:\Users\16276\Desktop\C1BC4674E777233EE3D5374779A170BA.jpg')
    face_engine = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    # 灰度处理
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faecs = face_engine.detectMultiScale(img,scaleFactor=1.2,minNeighbors=10)
    for (x,y,w,h) in faecs:
        # 框出脸，画笔宽度为3
        img1=img[y:y+h,x:x+w]
        cv2.imshow('wsy3.png',img1)
        img = cv2.rectangle(img,(x,y),(x+204,y+204),(255,200,10),3)
        print(x,y,w,h)
    # 在名为sy的窗口中展示效果图
    cv2.imshow('sy',img)
    # 进行监听，若有任何按键，则退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 保存为wsy


def face_eyes_mouse():
    img = cv2.imread(r'C:\Users\16276\Desktop\C1BC4674E777233EE3D5374779A170BA.jpg')
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')
    eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
    smile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')

    faces = face_cascade.detectMultiScale(img,1.2,20)
    for (fx,fy,fw,fh) in faces:
        img = cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(0,200,200),2)
        face_area = img[fy:fy+fh,fx:fx+fw]
        eyes=eye_cascade.detectMultiScale(face_area,minNeighbors=40)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ex+eh),(0,255,0),1)
        smiles = smile.detectMultiScale(face_area,1.2,10)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(face_area,(sx,sy),(sx+sw,sy+sh),(0,0,255),3)
            cv2.putText(img, 'Smile', (fx, fy - 7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)

     # 在名为sy的窗口中展示效果图
    cv2.imshow('sy', img)
     # 进行监听，若有任何按键，则退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def live_classifier():
    #打开摄像头
    cap = cv2.VideoCapture(r'C:\Users\16276\Desktop\pbxd.mp4')
    #加载脸，眼睛，笑容的级联分类器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    n=1;
    while(True):
        #读取摄像头画面      画面为frame
        ret,frame = cap.read()
        #对联进行检测
        faces = face_cascade.detectMultiScale(frame, 1.2, 2)
        img = frame
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
        time.sleep(2)
        # n=n+1
        #显示出检测后的画面
        cv2.imshow('xupeng',img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    cap.release()


    cv2.destroyAllWindows()

def main():
    face()
    # face_eyes_mouse()
    # live_classifier()


if __name__ == '__main__':
    main()