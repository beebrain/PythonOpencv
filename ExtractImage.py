import cv2 
import numpy as np

cap = cv2.VideoCapture("thai_finger.mp4")
#cap = cv2.VideoCapture(0)
def nothing(x):

    pass


cv2.namedWindow("control",cv2.WINDOW_NORMAL)
cv2.createTrackbar("Hx", 'control',0,255,nothing)
cv2.createTrackbar("Hn", 'control',0,255,nothing)
cv2.createTrackbar("Sx", 'control',0,255,nothing)
cv2.createTrackbar("Sn", 'control',0,255,nothing)
cv2.createTrackbar("Vx", 'control',0,255,nothing)
cv2.createTrackbar("Vn", 'control',0,255,nothing)
count = 0
while(cap.isOpened()):

    ret, frame = cap.read()
    if ret!=True:
        break
    
    
    cv2.imshow('frame',frame)
    cv2.imwrite("Image/frame"+str(count)+".jpg", frame)     # save frame as JPEG file
    cv2.imshow("20sec",frame)   
    count = count+1
    
    if  cv2.waitKey(1) & 0xFF == ord('q') :
        break
 
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()


