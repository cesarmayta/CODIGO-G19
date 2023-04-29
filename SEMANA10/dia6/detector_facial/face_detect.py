import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)