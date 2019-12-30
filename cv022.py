import cv2
import time as t
camera_on=cv2.VideoCapture(0)
retrive,image=camera_on.read()
save_location="my image.jpg"
cv2.imwrite(save_location,image)
#t.sleep(5)
del camera_on
