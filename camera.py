import cv2
camera=cv2.VideoCapture(0)
check,detect=camera.read()
cv2.imwrite("picture.png",detect)
del camera
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
image=cv2.imread("picture.png")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
eyes=eye_cascade.detectMultiScale(gray_image,1.3,9)
for(x,y,w,h) in eyes:
    
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Eye detect",image)
cv2.waitKey()
cv2.destroyAllWindows()

