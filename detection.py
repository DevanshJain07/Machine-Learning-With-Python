import cv2
import numpy as np
eyes_detect=cv2.CascadeClassifier('haarcascade_eye.xml')
noise_detect=cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
face_detect=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
if face_detect.empty():
    raise IOError('Unable to haarcascade_frontalface_alt.xml file')
if eyes_detect.empty():
    raise IOError('Unable to haarcascade_eye.xml file')
if noise_detect.empty():
    raise IOError('Unable to haarcascade_mcs_nose.xml file')
capture=cv2.VideoCapture(0)
while True:

    ret,capturing=capture.read()
    x,y,w,h=0,0,0,0
    resize_frame=cv2.resize(capturing,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    gray=cv2.cvtcolor(resize_frame,cv2.COLOR_BGR2GRAY)
if face_detect.empty():
    raise IOERROR('Unable ')
    resize_frame=cv2.resize(capturing,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    gray=cv2.cvtcolor(resize_frame,cv2.COLOR_BGR2GRAY)
    face_detection=face_detect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face_detection:
        cv2.rectangle(resize_frame,(x,y),(x+w,y+h),(0,0,255),10)
