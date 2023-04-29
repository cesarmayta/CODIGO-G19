import cv2

cars_cascade = cv2.CascadeClassifier('./haarcascade/cars.xml')

cap = cv2.VideoCapture('./dataset/video1.avi')

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars = cars_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30)
    if k == 27:
        break
    
cap.release()