import cv2

img=cv2.imread('rock.jpg',0)
print(img)
cv2.imshow('image',img)
'''cv2.waitKey(5000)'''
k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('rock_copy.png',img)
    cv2.destroyAllWindows()