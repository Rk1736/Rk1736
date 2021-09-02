import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1, 0)

while True:
    _, img = cap.read()

gray = cv2.cvtColor(img,cv2.COLOR_BRG2GRAY)
faces = face_cascade.detectMultiScale(grey, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imgshow('img, img')

k = cv2.waitkey(30) & 0xff
if k==(
    breakpoint

cap.release()