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

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret!=True:
        break
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #inRange(hsv, Scalar(0, 40, 60), Scalar(20, 150, 255), bw);
    #inRange(hsv, Scalar(0, 10, 60), Scalar(20, 150, 255), bw);
    hx = cv2.getTrackbarPos("Hx",'control')
    hn = cv2.getTrackbarPos("Hn",'control')
    sx = cv2.getTrackbarPos("Sx",'control')
    sn = cv2.getTrackbarPos("Sn",'control')
    vx = cv2.getTrackbarPos("Vx",'control')
    vn = cv2.getTrackbarPos("Vn",'control')
    
    cv2.rectangle(frame, (1,2), (255,255), (0,255,0), 2);
    lower_blue = np.array([hn, sn, vn])
    upper_blue = np.array([hx, sx, vx])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    
    #g = cv2.getTrackbarPos('G','frame')
    #b = cv2.getTrackbarPos('B','frame')
    
    if  cv2.waitKey(1) & 0xFF == ord('q') :
        break
 
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()


